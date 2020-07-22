##################################
### Building a basic flask app ###
##################################

from flask import Flask
from flask import render_template   # rendering html files
from flask import url_for           # rendering static css files
from flask import flash             # for flashing messages (modifications made to layout.html template for this)
from flask import redirect          # redirect to another route url
from forms import RegistrationForm, LoginForm   # Importing forms from forms.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b01a54d78abbef243757547790d122ea'   # Convert this to environment variable later...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'     # Relative path to the current file
db = SQLAlchemy(app)    # SQLAlchemy database instance (pass your app as an arg when creating)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)    # Post attribute has a relationship to the post model

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# The variable 'posts' simulates a database response (two posts shown here)
# i.e. this is dummy data
posts = [
    {
        'author': 'Luis Lopez',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 4, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 14, 2020'
    }
]

@app.route('/hello')
def hello_world():
    return '<h1>Hello, world!</h1>'     # Renders valid HTML


@app.route('/')         # Decorator used to map URLs to functions
@app.route('/home')     # You can have multiple routes to the same page
def index():
    # return 'Index Page (this is my HOME page)'    # Non-template rendering
    return render_template('home.html')     # Searches for html file in 'templates' dir


@app.route('/about')
def about():
    # return '<h1>About page</h1>'
    return render_template('about.html', title='About')

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts)

@app.route('/tomato')
def tomato():
    return render_template('tomatoes.html', title='Tomato page for tomato heads')

###################
### FORM ROUTES ###
###################
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Create an instance of your RegistrationForm to pass to a template
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('blog'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Create an instance of your RegistrationForm to pass to a template
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data  == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('blog'))
        else:
            flash('Login attempt unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':      # This conditional runs in Flask app in debug
    app.run(debug=True)         # mode if script is being ran directly


