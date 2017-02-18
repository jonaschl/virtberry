from flask import Flask
from flask_login import LoginManager
from virtberryusers import User, check_if_user_exist
app = Flask(__name__)
app.config.from_object('config')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message_category = "alert-danger"
from app import views
from app import actions
from app import login
from app import logout
from app import preferences
from app import errors

@login_manager.user_loader
def load_user(user_id):
    print (user_id)
    if check_if_user_exist(user_id) == True:
        user = User(user_id)
        return user
    else:
        return None
