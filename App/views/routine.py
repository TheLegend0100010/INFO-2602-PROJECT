from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash, url_for
from App.models import db, Routine
from flask_jwt_extended import current_user
from App.controllers import edit_routine, make_routine, get_routine, save_routine, check_routine_saved
from flask_jwt_extended import jwt_required

routine_views = Blueprint('routine_views', __name__, template_folder='../templates')


@routine_views.route('/routine/<int:id>', methods=['GET'])
@jwt_required()
def view_routine(id):
    return render_template('templanding.html', routine=get_routine(id))

@routine_views.route('/routines', methods=['GET'])
@jwt_required()
def user_routines():
    return render_template('tempMYPOSTS.html')

@routine_views.route('/createroutine', methods=['GET'])
@jwt_required()
def create_routine_page():
    return render_template('templanding.html')

@routine_views.route('/routine', methods=['POST'])
@jwt_required
def create_routine():
    data = request.form
    routine = make_routine(data['name'], current_user.id)
    flash('Routine created')
    return redirect(url_for('routine_views.view_routine', id=routine.id))


@routine_views.route('/routine', methods=['PUT'])
def edit_routine():
    data = request.form
    routine = edit_routine(data['id'], data['name'], data['text'])

@routine_views.route('/routine/save/<int:id>')
def save_routine_action(id):
    if check_routine_saved(id, current_user.id):
        save_routine(id, current_user.id)


