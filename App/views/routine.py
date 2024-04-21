from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash
from App.models import db
from flask_jwt_extended import current_user
from App.controllers import edit_routine, make_routine, get_routine

routine_views = Blueprint('routine_views', __name__, template_folder='../templates')


@routine_views.route('/routine/<int:id>', methods=['GET'])
def view_routine(id):
    return render_template('templanding.html', routine=get_routine(id))

@routine_views.route('/routine', methods=['POST'])
def create_routine():
    data = request.form
    routine = make_routine(data['name'], current_user.id)


@routine_views.route('/routine', methods=['PUT'])
def edit_routine():
    data = request.form
    routine = edit_routine(data['id'], data['name'], data['text'])

# @routine_views.route('/routine/list/<int:id>')
# def like_post(id):
#     like_routine


