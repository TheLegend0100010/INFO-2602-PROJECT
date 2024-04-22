from App.database import db
from .routine import Routine

class Workout(db.Model):
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(500), nullable = False)
    level = db.Column(db.String(200), nullable = False)
    
    def __init__(self, name, level):
        self.name = name
        self.level = level

