from flask import Flask
from flask_login import LoginManager
from .user import User
app = Flask(__name__)
app.config.from_object('config')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
from app import views
from app import actions
from app import test

@login_manager.user_loader
def load_user(user_id):
    print (user_id)
    if user_id == "hello":
        user = User(user_id)
        return user
    else:
        return None
