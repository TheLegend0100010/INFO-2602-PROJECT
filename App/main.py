import os
from flask import Flask, render_template
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

from App.database import init_db
from App.config import load_config

from App.controllers import (
    setup_jwt,
    add_auth_context
)

from App.views import views

def add_views(app):
    for view in views:
        app.register_blueprint(view)

def create_app(overrides={}):
    app = Flask(__name__, static_url_path='/static')
    load_config(app, overrides)
    CORS(app)
    add_auth_context(app)
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app)
    init_db(app)
    jwt = setup_jwt(app)
    
    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def custom_unauthorized_response(error):
        return render_template('401.html', error=error), 401
    
    app.app_context().push()
    return app




def create_users():
    rob = User(username="rob", email = "robemail@gmail.com" , password="robpass")
    bob = User(username="bob", email = "bobemail@gmail.com" , password="bobpass")
    sally = User(username="sally", email = "sallyemail@gmail.com" , password="sallypass")
    pam = User(username="pam", email = "pamemail@gmail.com" , password="pampass")
    chris = User(username="chris", email = "chrisemail@gmail.com" , password="chrispass")
    db.session.add_all([rob, bob])
    db.session.commit()

def getCategory():
    legs = Workout(id=1 , name = "Legs")
    arms = Workout(id=2 , name = "Arms")
    chest = Workout(id=3 , name = "Chest")
    back = Workout(id=4 , name = "Back")
    shoulders = Workout(id=5 , name = "Shoulders")

    db.session.add_all([legs, arms, chest, back, shoulders])
    db.session.commit()

    @app.route('/')
def login():
  return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_action():
  username = request.form.get('username')
  password = request.form.get('password')
  user = User.query.filter_by(username=username).first()
  if user and user.check_password(password):
    response = redirect(url_for('home'))
    access_token = create_access_token(identity=user.id)
    set_access_cookies(response, access_token)
    return response
  else:
    flash('Invalid username or password')
    return redirect(url_for('login'))



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
