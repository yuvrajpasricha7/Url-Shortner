from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length
from wtforms import StringField,PasswordField,SubmitField


class RegForm(FlaskForm):
    username=StringField('Username:', validators=[DataRequired(),Length(min=5,max=9,message='Username must be between 5 to 9 characters long!')])
    password=PasswordField('Password:', validators=[DataRequired(),Length(min=8,message='Password should be atleast 8 characters long!')])
    submit=SubmitField('Sign up')

class LoginForm(FlaskForm):
    username=StringField('Username:', validators=[DataRequired(),Length(min=5,max=9)])
    password=PasswordField('Password:', validators=[DataRequired(),Length(min=8)])
    submit=SubmitField('Login')

class UrlForm(FlaskForm):
    urls=StringField('url',validators=[DataRequired()])
    submit=SubmitField('Short url')