# Building a basic flask app

from flask import Flask
from flask import render_template
from flask import url_for   # For rendering static css files

app = Flask(__name__)

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

if __name__ == '__main__':      # This conditional runs in Flask app in debug
    app.run(debug=True)         # mode if script is being ran directly


