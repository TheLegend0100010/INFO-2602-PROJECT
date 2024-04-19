from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .routine import Routine

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable = False)
    age = db.Column(db.Integer, nullable = True)
    weight = db.Column(db.Integer, nullable = True)
    routines = db.relationship('Routine', backref = "user", lazy = True)
    

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.email = "TEST"
        

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
