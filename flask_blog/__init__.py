
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b01a54d78abbef243757547790d122ea'   # Convert this to environment variable later...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'     # Relative path to the current file
db = SQLAlchemy(app)    # SQLAlchemy database instance (pass your app as an arg when creating)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # This is the function name of the route (same thing you pass into url_for)
login_manager.login_message_category = 'info'   # Bootstrap class (blue-colored theme thing) - nicer alerts/messages

from flask_blog import routes