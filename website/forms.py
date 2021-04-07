from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length


class Register(Form):
    name = StringField(
        'Name', validators=[DataRequired()]
    )
    email = StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    password1 = StringField(
        'Password', validators=[DataRequired()]
    )
    password2 = StringField(
        'Confirm Password', validators=[DataRequired()]
    )


class Login(Form):
    email = StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    password = StringField(
        'Password', validators=[DataRequired()]
    )


class Todo(Form):
    todo = TextAreaField(
        'Add Todo', validators=[DataRequired()]
    )
