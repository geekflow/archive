#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    .index
    ~~~~~~~~~~~~~~~~~

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from flask import redirect, url_for, send_from_directory 
from os.path import join

from .blueprint import frontend
from .controller.login import login_required

@frontend.record
def record(setup_state):
    global root_path
    app = setup_state.app
    root_path = app.root_path

@frontend.route('/')
@login_required
def index():
    return redirect(url_for('.getList'))

@frontend.route('/favicon.ico')
def favicon():
    return send_from_directory(join(root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')