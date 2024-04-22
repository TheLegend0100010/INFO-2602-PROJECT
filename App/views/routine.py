from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash, url_for
from App.models import db, Routine, Workout
from flask_jwt_extended import current_user
from App.controllers import add_workout, delete_routine_action, edit_routine, make_routine, get_routine, save_routine, check_routine_saved, unsave_routine
from flask_jwt_extended import jwt_required

routine_views = Blueprint('routine_views', __name__, template_folder='../templates')


@routine_views.route('/routine/<int:id>', methods=['GET'])
@jwt_required()
def view_routine(id):
    return render_template('temp POST file.html', routine=get_routine(id))

@routine_views.route('/routine/add/<int:id>/<int:workoutid>')
@jwt_required()
def add_workout_action(id, workoutid):
    routine = Routine.query.get(id)
    if routine.user_id == current_user.id:
        add_workout(id, workoutid)
    return redirect(url_for('index_views.home'))
    
@routine_views.route('/saved', methods=['GET'])
@jwt_required()
def view_saved_routine():
    return render_template('temp sabed.html')

@routine_views.route('/routines', methods=['GET'])
@jwt_required()
def user_routines():
    return render_template('tempMYPOSTS.html')

@routine_views.route('/createroutine', methods=['GET'])
@jwt_required()
def create_routine_page():
    return render_template('temp POST file.html')

@routine_views.route('/routine', methods=['POST'])
@jwt_required()
def create_routine():
    data = request.form
    routine = make_routine(data['name'], data['text'], current_user.id)
    flash('Routine created')
    return redirect(url_for('routine_views.user_routines'))

@routine_views.route('/add/<int:id>', methods=['GET'])
@jwt_required()
def add_workout_page(id):
    return render_template('addd.html', workout=Workout.query.filter_by(id=id).first())

@routine_views.route('/routine/delete/<int:id>', methods=['POST'])
@jwt_required()
def delete_routine(id):
    if delete_routine_action(id, current_user.id):
        flash('Routine Deleted')
    else: 
        flash('You cannot delete this routine')
    return redirect(url_for('routine_views.user_routines'))


@routine_views.route('/routine/edit/<int:id>', methods=['GET'])
@jwt_required()
def edit_page(id):
    return render_template('edit.html', routine=Routine.query.filter_by(id=id).first())

@routine_views.route('/editroutine/<int:id>', methods=['POST'])
@jwt_required()
def edit_routine_route(id):
    data = request.form
    routine = edit_routine(id, data['name'], data['text'])
    return redirect(url_for('routine_views.user_routines'))

@routine_views.route('/routine/save/<int:id>', methods=['POST'])
def save_routine_action(id):
    if check_routine_saved(id, current_user.id):
        save_routine(id, current_user.id)
    else: unsave_routine(id, current_user.id)
    return request.referrer


