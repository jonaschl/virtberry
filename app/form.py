from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class ChangePassword(FlaskForm):
    passwordold = PasswordField('passwordold', validators=[DataRequired()])
    passwordnew1 = PasswordField('passwordnew1', validators=[DataRequired()])
    passwordnew2 = PasswordField('passwordnew2', validators=[DataRequired()])
