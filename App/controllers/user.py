from App.models import User, Routine
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
    current_user
)

def create_user(username, password):
    new_user = User(username=username, password=password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except IntegrityError:
        db.session.rollback()
        return None

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        token = create_access_token(identity=user.username)
        return token
    return None

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def check_routine_saved(id, routineID):
    user = User.query.get(id)
    if user:
        routine = Routine.query.get(routineID)
        for routinee in user.routines:
            if routine.id == routinee.id:
                return True
    return False
            
# def checkSaved(id, routineID):
#     user = User.query.filter_by(id = id).first()
#     if user:
#         for routine in user.routines:
#             if routine.id == routineID and routine.user_id == user.id:
#                 return True
#     return False