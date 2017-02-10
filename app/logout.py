from flask import render_template, redirect, url_for, flash
from app import app
import flask_login
from flask_login import LoginManager, login_required, logout_user, current_user


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
