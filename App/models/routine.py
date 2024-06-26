from App.database import db
class Routine(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = False)
    text = db.Column(db.String(500), nullable = True)
    level = db.Column(db.String(50), nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    saves = db.Column(db.Integer, nullable = False)
    workouts = db.relationship('Workout', secondary = 'routine_workout', backref= 'routines', lazy = True)

    def __init__(self, name, text, user_id):
        self.name = name
        self.text = text
        self.user_id = user_id
        self.saves = 0
        self.level = 'Beginner'

    