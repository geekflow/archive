#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    .model.init
    ~~~~~~~~~~~~~~

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

__all__ = ['user', 'search', 'database']
