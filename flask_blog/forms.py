from flask_wtf import FlaskForm  # Writing python classes that are representative of our forms (EXTEND this)
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField  # The kind of form field
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError  # VALIDATORS also come as classes
from flask_blog.models import User

# Say you want to make a registration form - create registration class
class RegistrationForm(FlaskForm):  # Extend the FlaskForm class for form creation
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')     # You need a submit button

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please enter a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken. Please enter a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])     # Using email to log in
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')     # You need a submit button


class UpdateAccountForm(FlaskForm):  # Extend the FlaskForm class for form creation
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')     # You need a submit button

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is already taken. Please enter a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already taken. Please enter a different one.')


