from  App.database import db

class RoutineWorkout(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))