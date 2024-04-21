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
    routine = Routine.query.get(routineID)
    if routine:
        routine.name = name
        routine.text = text
        db.session.add(routine)
        db.session.commit()
        return routine
    return None

def add_workout(routineID, workoutID):
    routine = Routine.query.get(routineID)
    if routine:
        workout = Workout.query.get(workoutID)
        if workout:
            if routine.level == 'beginner':
                routine.level = workout.level
            elif routine.level == 'intermediate' and workout.level == 'expert':
                routine.level = workout.level
            routine.workouts.append(workout)
            db.session.add(routine)
            db.session.commit()
            return routine
    return None

def save_routine(routineID, user_id):
    routine = Routine.query.get(routineID)
    if routine:
        user = User.get(user_id)
        if user and routine.user_id != user_id:
            user.routines.append(routine)
            routine.saves += 1
            db.session.add(user)
            db.session.commit()
        return user
    return None

def unsave_routine(routineID, user_id):
    routine = Routine.query.get(routineID)
    if routine:
        user = User.query.get(user_id)
        if user and routine in user.routines:
            user.routines.remove(routine)
            routine.saves -= 1
            db.session.commit()
            return True
    return False

