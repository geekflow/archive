#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    wiki
    ~~~~~~~~~

    writing module for markdown format similar wiki.

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from flask import Flask, session, redirect, request, url_for 
from flask import render_template, abort
from jinja2 import TemplateNotFound
from werkzeug import generate_password_hash
from wtforms import Form, TextField, PasswordField, HiddenField, validators
from ..blueprint import frontend
from ..util.logger import Log
from ..model.database import DBManager as db
from ..model.user import User

import markdown

@frontend.route('/user')
@frontend.route('/user/<name>', methods=['GET', 'POST'])
def show(name=None):
    try:
        if request.method == 'POST':
            return "Hello World2!"
        return markdown.markdown(render_template("index.html", name=name))
    except TemplateNotFound:
        abort(404)
        
@frontend.route('/signup', methods=['GET'])
@frontend.route('/user/signup', methods=['GET'])
def signupForm():
    form = RegistrationForm(request.form)
    
    try:
        return render_template('signup.html', form = form)
    except TemplateNotFound:
        abort(404)
        
@frontend.route('/signup', methods=['POST'])
@frontend.route('/user/signup', methods=['POST'])
def signup():
    form = RegistrationForm(request.form)
    
    if form.validate():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        
        try:
            user = User(email, username, generate_password_hash(password))
            db.session().add(user)
            db.session().commit()
        except Exception as e:
            error = "DB error occurs : " + str(e)
            Log.error(error)
            db.session().rollback()
            raise e
        else:
            return redirect(url_for('.login', email=email)) 
    else:
        return render_template('signup.html', form = form)
        
class RegistrationForm(Form):
    email = TextField('email',
                  [validators.Required('Email을 입력하세요.'),
                   validators.Length(min=7, max=100, message='7자리 이상 100자리 이하로 입력하세요.')])
    
    username = TextField('username',
                  [validators.Required('이름을 입력하세요.'),
                   validators.Length(min=2, max=50, message='2자리 이상 50자리 이하로 입력하세요.')])
    
    password = PasswordField('New Password',
                [validators.Required('비밀번호를 입력하세요.'),
                 validators.Length(min=5, max=100, message='6자리 이상 100자리 이하로 입력하세요.')])
    
    next_url = HiddenField('Next URL')