from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash, url_for
from App.models import db, Workout, Routine
from App.controllers import create_user, login_user
import json
from flask_jwt_extended import jwt_required, set_access_cookies

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('templanding.html')

@index_views.route('/signup', methods=['GET'])
def signup():
     return render_template('tempsignup.html')

@index_views.route('/home', methods=['GET'])
@jwt_required()
def home():
    return render_template('tempHome.html', routines = Routine.query.all())

@index_views.route('/signup', methods=['POST'])
def signup_action():
    data = request.form
    user = create_user(data['username'], data['password'])
    if user:
        flash("User created")
        token = login_user(user.username, data['password'])
        response = redirect(url_for('index_views.home'))
        set_access_cookies(response, token)
        if token:
            return response
        flash('Error logging in')
        return render_template('templogin.html')
    flash("Username already taken")
    return render_template('tempsignup.html')



@index_views.route('/login', methods=['GET'])
def login():
     return render_template('templogin.html')

@index_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    token = login_user(data['username'], data['password'])
    if token:
        response = redirect(url_for('index_views.home'))
        set_access_cookies(response, token)
        flash("Logged In")
        return response
    flash("Invalid username/password")
    return render_template('templogin.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    with open('exercises.json', encoding = "utf-8") as file:
        exercises = json.load(file)
        records =[]
        for exercise in exercises['exercises']:
            image = exercise['name'].replace(' ', '_')
            image = image.replace('/', '_')
            imagelink = f"https://raw.githubusercontent.com/wrkout/exercises.json/master/exercises/{image}/images/0.jpg"
            instructions = ""
            for instruct in exercise['instructions']:
                    instructions += instruct
            record = Workout(exercise['name'], exercise['level'], exercise['primaryMuscles'][0], imagelink)
            records.append(record)
            db.session.bulk_save_objects(records)
            db.session.commit()
    return jsonify(message='db initialized!')

@index_views.route('/workout', methods=['GET'])
def workouts_page():
     flash('Win')
     return render_template('templanding.html')
    # return jsonify(message="Page Not Implemented Yet")


@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})