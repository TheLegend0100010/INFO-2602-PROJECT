from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db, Workout
from App.controllers import create_user
import json

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

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
    return jsonify(message="Page Not Implemented Yet")


@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})