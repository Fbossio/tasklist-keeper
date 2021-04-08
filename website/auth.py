from flask import Flask, Blueprint, render_template, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .forms import Register, Login

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    return '<h1>Nothing Yet</h1>'


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = Register()
    return render_template('signup.html', form=form)
