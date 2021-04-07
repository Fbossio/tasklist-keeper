from flask import Flask, Blueprint, render_template, url_for
from flask_login import login_required, current_user
from .models import Todo
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home('/'):
    return render_template('home.html')
