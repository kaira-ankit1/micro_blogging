from flask import Flask
from flask_socketio import SocketIO, emit
from flask_login import LoginManager 
from db.Connection import db
from model.user import User
from routes import *
app = Flask(__name__)
app.register_blueprint(routes)
app.config['SECRET_KEY'] = 'hujjjhjjhgghgjh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

socketio = SocketIO(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()
    db.session.commit()

@socketio.on('connect')
def on_connect():
    if current_user.is_anonymous:
        return False
    emit('welcome', {'username': current_user.username})

if __name__ == "__main__":
    app.run()