#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    .blueprint
    ~~~~~~~~~~~~~~~~~~

    archive blueprint module.

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from flask import Blueprint
from .util.logger import Log

frontend = Blueprint('frontend', __name__, template_folder='templates', static_folder='static')

Log.debug('static folder : %s' % frontend.static_folder)
Log.debug('template folder : %s' % frontend.template_folder)