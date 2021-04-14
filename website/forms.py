from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo


class Register(FlaskForm):
    name = StringField(
        'Name', validators=[DataRequired(), InputRequired()]
    )
    email = StringField(
        'Email', validators=[DataRequired(), InputRequired(), Email()]
    )
    password1 = PasswordField(
        'Password', validators=[DataRequired(), InputRequired(), Length(min=7), EqualTo('password2', message='Passwords must match.')]
    )
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), InputRequired()]
    )


class Login(FlaskForm):
    email = StringField(
        'Email', validators=[DataRequired(), InputRequired()]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), InputRequired()]
    )


class Task(FlaskForm):
    todo = TextAreaField(
        'Enter a new task', validators=[DataRequired(), InputRequired()]
    )
