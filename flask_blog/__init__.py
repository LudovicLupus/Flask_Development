
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b01a54d78abbef243757547790d122ea'   # Convert this to environment variable later...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'     # Relative path to the current file
db = SQLAlchemy(app)    # SQLAlchemy database instance (pass your app as an arg when creating)
bcrypt = Bcrypt(app)

from flask_blog import routes