from flask import render_template, redirect, url_for, flash
from flask_httpauth import HTTPBasicAuth
from app import app

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None
