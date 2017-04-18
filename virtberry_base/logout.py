from flask import render_template, redirect, url_for, flash
from virtberry_base import virtberry_base
from flask_login import LoginManager, login_required, logout_user, current_user


@virtberry_base.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
