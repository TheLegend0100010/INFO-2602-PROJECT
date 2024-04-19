from App.database import db
class Routine(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    category = db.Column(db.String(999), nullable= False)
    name = db.Column(db.String(50), nullable = False)
    text = db.Column(db.String(500), nullable = True)
    level = db.Column(db.String(50), nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    