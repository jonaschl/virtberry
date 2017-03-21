from flask import Flask
from flask_login import LoginManager
from virtberryusers import User, check_if_user_exist
app = Flask(__name__)
app.config.from_object('config')
import virtberry_module_management
from virtberry_module_management import *

for module in get_enabled_modules():
    # import the real module (the code)
    the_real_module = import_module_from_name(module)
    # create a objet from the virtberry_module class
    the_module = virtberry_module(module)
    for blueprint in the_module.get_attributes('blueprints'):
        app.register_blueprint(get_object_from_name(the_real_module, blueprint))

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
