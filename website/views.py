from flask import Flask, Blueprint, render_template, url_for
from flask_login import login_required, current_user
from .models import Todo
from . import db

views = Blueprint('views', __name__)


@views.route('/todo', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', user=current_user)
