#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    test_url_for
    ~~~~~~~~~

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

'''
from flask import request, Response
from geeksaga.archive import create_app

app = create_app()

with app.test_request_context('/?name=Peter'):
    assert request.path == '/'
    assert request.args['name'] == 'Peter'

if __name__ == '__main__':
    with app.test_request_context('/archive/list'):
        resp = Response('...')
        print(resp)
        resp = app.process_response(resp)
        print(resp)
        print(request)
'''