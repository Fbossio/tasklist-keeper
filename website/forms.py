from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, Email


class Register(FlaskForm):
    name = StringField(
        'Name', validators=[DataRequired(), InputRequired()]
    )
    email = StringField(
        'Email', validators=[DataRequired(), InputRequired(), Email()]
    )
    password1 = PasswordField(
        'Password', validators=[DataRequired(), InputRequired(), Length(min=7)]
    )
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), InputRequired()]
    )


class Login(FlaskForm):
    email = StringField(
        'email', validators=[DataRequired(), InputRequired()]
    )
    password = PasswordField(
        'password', validators=[DataRequired(), InputRequired()]
    )


class Todo(FlaskForm):
    todo = TextAreaField(
        'todo', validators=[DataRequired()]
    )
