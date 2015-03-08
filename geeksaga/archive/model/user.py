#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    .model.user
    ~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    username = Column(String(50), unique=True)
    password = Column(String(100), unique=False)

#    geeks = relationship('Geeks', 
#                          backref='user', 
#                          cascade='all, delete, delete-orphan')
    
    def __init__(self, email, name, password):
        self.email = email
        self.username = name
        self.password = password

    def __repr__(self):
        return '<User %r %r>' % (self.email, self.username)