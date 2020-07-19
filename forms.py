from flask_wtf import FlaskForm  # Writing python classes that are representative of our forms (EXTEND this)
from wtforms import StringField, PasswordField, SubmitField, BooleanField  # The kind of form field
from wtforms.validators import DataRequired, Length, Email, EqualTo  # VALIDATORS also come as classes


# Say you want to make a registration form - create registration class
class RegistrationForm(FlaskForm):  # Extend the FlaskForm class for form creation
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')     # You need a submit button


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])     # Using email to log in
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')     # You need a submit button




