from flask import Flask, Blueprint, render_template, url_for, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Todo
from . import db
from .forms import Task
from .helpers import flash_errors

views = Blueprint('views', __name__)


@views.route('/todo', methods=['GET', 'POST'])
@login_required
def home():
    form = Task()
    if form.validate_on_submit():
        todo = request.form.get('todo')
        try:
            new_task = Todo(task=todo, user_id=current_user.id)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('views.home'))

        except AssertionError as error:
            flash(error, category='error')
    else:
        flash_errors(form)

    return render_template('home.html', form=form, user=current_user, data=Todo.query.filter_by(user_id=current_user.id).order_by('id').all())


@views.route('/delete-todo/<todoId>', methods=['DELETE'])
def delete_todo(todoId):
    todo = Todo.query.get(todoId)
    if todo:
        db.session.delete(todo)
        db.session.commit()

    return jsonify({})


@views.route('/update-todo/<todoId>', methods=["POST"])
def update_todo(todoId):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todoId)
        todo.completed = completed
        db.session.commit()

    except AssertionError as error:
        flash(error, category='error')
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({})
