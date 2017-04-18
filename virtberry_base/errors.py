#!/usr/bin/python3
from flask import render_template
from virtberry_base import virtberry_base

@virtberry_base.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@virtberry_base.errorhandler(403)
def page_not_found(e):
    return render_template('errors/403.html'), 403
