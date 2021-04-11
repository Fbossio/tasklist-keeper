from flask import Flask, Blueprint, render_template, url_for, request, flash, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .forms import Register, Login
from .helpers import flash_errors

auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('User does not exist', category='error')
    else:
        flash_errors(form)

    return render_template('login.html', form=form, user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


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
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    else:
        flash_errors(form)

    return render_template('signup.html', form=form, user=current_user)
