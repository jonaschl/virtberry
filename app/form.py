from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
