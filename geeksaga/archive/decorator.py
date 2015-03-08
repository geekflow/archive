# -*- coding: utf-8 -*-
"""
    .decorator
    ~~~~~~~~~

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
from functools import wraps
from flask import request, session, redirect, url_for, abort, g
from flask import render_template
from geeksaga.archive.util.logger import Log
#from werkzeug.contrib.cache import SimpleCache
#cache = SimpleCache()
#from werkzeug.contrib.cache import MemcachedCache
#cache = MemcachedCache(['127.0.0.1:11211'])
#from werkzeug.contrib.cache import GAEMemcachedCache
#cache = GAEMemcachedCache()

def login_required(f):
    """
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            is_login = False
            if 'user_info' in session:
                is_login = True
            if not is_login:
                return redirect(url_for('.login', next=request.url))
            return f(*args, **kwargs)
        except Exception as e:
            Log.error("login required error occurs : %s" % str(e))
            raise e
    return decorated_function

def user_required(f):
    """Checks whether user is logged in or raises error 401."""
    def decorator(*args, **kwargs):
        print('user_required')
        #if not g.user:
        #    abort(401)
        return f(*args, **kwargs)
    return decorator

'''
def cached(timeout=5 * 60, key='view/%s'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key % request.path
            rv = cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, timeout=timeout)
            return rv
        return decorated_function
    return decorator
'''

def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            
            print(template_name)
            
            if template_name is None:
                template_name = request.endpoint.replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator