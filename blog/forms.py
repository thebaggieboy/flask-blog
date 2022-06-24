import email
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User
from flask_login import current_user

class PostForm(FlaskForm):
    title = StringField('Title',   validators=[DataRequired()])
    content = TextAreaField('Content', render_kw={'rows': 10}, validators=[DataRequired()])
    submit = SubmitField('Post')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
             validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email Address',
             validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Theres already an account with this username, please choose another.')
    def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Theres already an account with this email, please choose another.')

    def __repr__(self):
        return self.email


class LoginForm(FlaskForm):
    email = StringField('Email Address',
             validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

    def __repr__(self):
        return self.email



class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
             validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email Address',
             validators=[DataRequired(), Email()])
    profile_picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'heic', 'webp'])])
   
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Theres already an account with this username, please choose another.')
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Theres already an account with this email, please choose another.')

    def __repr__(self):
        return self.email
