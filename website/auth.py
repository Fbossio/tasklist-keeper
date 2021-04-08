from flask import Flask, Blueprint, render_template, url_for, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .forms import Register, Login
from .helpers import flash_errors

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
    if form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password1')
        user = User.query.filter_by(email=email).first()

        if user:
            flash('User already exists!', category='error')
        else:
            new_user = User(name=name, email=email, password=generate_password_hash(
                password1, method='sha256'))
            return redirect(url_for('views.home'))
    else:
        flash_errors(form)

    return render_template('signup.html', form=form)
