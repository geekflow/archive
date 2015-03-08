#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    .util
    ~~~~~~~~~~~~~~~~~~~

    archive util initialize module. 

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

__all__ = ['logger', 'md']

import markdown

md = markdown.Markdown(
    extensions = ['tables'],
    safe_mode = False,
    smart_emphasis = False
)