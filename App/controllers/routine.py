from App.models import Routine, Workout, User
from App.database import db

def get_routine(id):
    try:
        routine = Routine.query.get(id)
    except Exception:
        return None
    return routine

def make_routine(name, user_id):
    routine = Routine(name, user_id)
    db.session.add(routine)
    db.session.commit()
    return routine

def edit_routine(routineID, name, text):
    routine = Routine.get(routineID)
    if routine:
        routine.name = name
        routine.text = text
        db.session.add(routine)
        db.session.commit()
        return routine
    return None

def add_workout(routineID, workoutID):
    routine = Routine.get(routineID)
    if routine:
        workout = Workout.get(workoutID)
        if workout:
            routine.workouts.append(workout)
            db.session.add(routine)
            db.session.commit()
            return routine
    return None

def save_routine(routineID, num, user_id):
    routine = Routine.get(routineID)
    if routine:
        user = User.query.filter_by(id=user_id)
        user.routines.append(routine)
        db.session.add(user)
        db.session.commit()
        return True
    return False
