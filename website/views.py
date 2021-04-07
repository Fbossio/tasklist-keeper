from flask import Flask, Blueprint, render_template
from flask_login import login_required, current_user
from .models import Todo
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
