from App.database import db
from .routine import Routine

class Workout(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    level = db.Column(db.String(20), nullable = False)
    
    def __init__(self, name, level, muscle, image):
        self.name = name
        self.level = level

