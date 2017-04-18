from flask import render_template, redirect, url_for, flash, current_app
from virtberry_base import virtberry_base
from virtberry_base.form import LoginForm
from flask_login import LoginManager, login_required, login_user, current_user
from virtberryusers import User

@virtberry_base.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # We need a check if the user actually exist
        user = User(form.user.data)
        user.check_pass(form.password.data)
        user.printdata()
        if user.is_authenticated() == True:
            if login_user(user)  == True:
                flash("Hello {}".format(current_user.get_user_name()))
                return redirect(current_app.login_redirect_to)
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
