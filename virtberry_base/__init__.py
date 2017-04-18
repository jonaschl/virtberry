from flask import Flask, current_app
from flask_login import LoginManager
from virtberryusers import User, check_if_user_exist
from virtberry_module_management import *
from virtberry_menu import *


# create app
virtberry_base = Flask(__name__)

# read config
# read config
PathToNormalConfigFile = "/etc/virtberry/config.json"

def get_flask_config():
    with open(PathToNormalConfigFile) as file:
        data = json.load(file)
        config = data.get("flask_config", {})
        return config

def get_redirect_login():
    with open(PathToNormalConfigFile) as file:
        data = json.load(file)
        data = data.get("login_config")
        return data.get("redirect_to")

virtberry_base.config.update(get_flask_config())
# set view which is displayed after login
virtberry_base.login_redirect_to = get_redirect_login()
#register blueprints
for module in get_enabled_modules():
    # import the real module (the code)
    the_real_module = import_module_from_name(module)
    # create a objet from the virtberry_module class
    the_module = virtberry_module(module)
    for blueprint in the_module.get_attributes('blueprints'):
        virtberry_base.register_blueprint(get_object_from_name(the_real_module, blueprint))

# register login manager
login_manager = LoginManager()
login_manager.init_app(virtberry_base)
login_manager.login_view = "login"
login_manager.login_message_category = "alert-danger"

@login_manager.user_loader
def load_user(user_id):
    if check_if_user_exist(user_id) == True:
        user = User(user_id)
        return user
    else:
        return None

# register menu
menu = Menu()
menu.init_app(virtberry_base)

# login and logout view
from virtberry_base import login
from virtberry_base import logout
#errors
from virtberry_base import errors
