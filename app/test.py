from flask import render_template, redirect, url_for, flash
from app import app
from .form import LoginForm
from .user import User
import flask_login
from flask_login import LoginManager, login_required, login_user, current_user



# index view function suppressed for brevity

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(form.user.data)
        user.check_pass(form.password.data)
        user.printdata()
        if user.is_authenticated() == True:
            if login_user(user)  == True:
                flash("Hello {}".format(current_user.get_user_name()))
                return redirect(url_for('index'))
            else:
                return render_template('login.html',
                               title='Sign In',
                               form=form)

        else:
            return render_template('login.html',
                           title='Sign In',
                           form=form)
    else:
            return render_template('login.html',
                           title='Sign In',
                           form=form)
