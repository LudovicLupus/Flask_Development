
from flask import render_template   # rendering html files
from flask import url_for           # rendering static css files
from flask import flash             # for flashing messages (modifications made to layout.html template for this)
from flask import redirect          # redirect to another route url
from flask_blog.forms import RegistrationForm, LoginForm   # Importing forms from forms.py
from flask_blog.models import User, Post
from flask_blog import app

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