
from flask import render_template   # rendering html files
from flask import url_for           # rendering static css files
from flask import flash             # for flashing messages (modifications made to layout.html template for this)
from flask import redirect          # redirect to another route url
from flask_blog.forms import RegistrationForm, LoginForm   # Importing forms from forms.py
from flask_blog.models import User, Post
from flask_blog import app, db, bcrypt
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user    # For accessing the logged-in user

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
    if current_user.is_authenticated:
        flash(f'Already logged in!')
        return redirect(url_for('blog'))
    # Create an instance of your RegistrationForm to pass to a template
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash(f'Already logged in!')
        return redirect(url_for('blog'))
    # Create an instance of your RegistrationForm to pass to a template
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('blog'))
        else:
            flash('Login attempt unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('blog'))


