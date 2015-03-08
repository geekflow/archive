#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    runserver
    ~~~~~~~~~

    develop server execute module for local test

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from flask import redirect, url_for
from geeksaga.archive import create_app

app = create_app()

from geeksaga.archive.controller import ArchiveAPI
archive_view = ArchiveAPI.ArchiveAPI.as_view('archive_api')
app.add_url_rule('/archive', view_func=archive_view, methods=['GET',])

#app.add_url_rule('/archive', view_func=archive_view, methods=['GET'])
#app.add_url_rule('/archive/<path:page>', view_func=archive_view, methods=['PUT'])

@app.route('/')
def index():
    #redirect to the about page
    return redirect('/archive')

def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])

#register_api(UserAPI, 'user_api', '/users/', pk='user_id')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt as e:
        pass