# -*- coding: utf-8 -*-
"""
    .__init__
    ~~~~~~~~~

    geeksaga archive init.

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

#from hashlib import md5

import sqlite3, os

def print_settings(config):
    print('========================================================')
    print('SETTINGS for GEEKSAGA APPLICATION')
    print('========================================================')
    for key, value in config:
        print('%s=%s' % (key, value))
    print('========================================================')

#@app.errorhandler
def page_not_found(error):
    return render_template('404.html'), 404

def server_error(error):
    err_msg = str(error)
    return render_template('500.html', err_msg=err_msg), 500

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

def create_app(config_filepath='resource/config.cfg'):
    app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')
    
    from .config import Config
    app.config.from_object(Config)
    app.config.from_pyfile(config_filepath, silent=True)
    
    from .util.logger import Log
    log_filepath = os.path.join(app.root_path, app.config['LOG_FILE_PATH'])
    Log.init(log_filepath=log_filepath)
    
    from .model.database import DBManager as db
    db_url = app.config.get('DB_URL')
    
    Log.info(db_url)
    
    db.init(db_url, eval(app.config['DB_LOG_FLAG']))    
    db.init_db()
    
    #flash('Selected User was successfully deleted')
    
    from .controller import ArchiveAPI, user, admin
    from . import index
    
    from .blueprint import frontend
    app.register_blueprint(frontend)
    
    # SessionInterface 설정.
    # Redis를 이용한 세션 구현은 cache_session.RedisCacheSessionInterface 임포트하고
    # app.session_interface에 RedisCacheSessionInterface를 할당
#    from geeks.cache_session import SimpleCacheSessionInterface
#    app.session_interface = SimpleCacheSessionInterface()
    
    app.error_handler_spec[None][404] = page_not_found
    app.error_handler_spec[None][500] = server_error
    
    app.jinja_env.globals['url_for_other_page'] = url_for_other_page
    
    SITE_ROOT = os.path.abspath(os.path.dirname(__file__))

    app.config.update(dict(
                           DATABASE=os.path.join(app.root_path, 'geeks.db'),
                           DEBUG=True,
                           SECRET_KEY='geeksaga.com',
                           USERNAME='geeksaga@geeksaga.com',
                           PASSWORD='geeksaga',
                           ARCHIVE_PATH=os.path.join(SITE_ROOT, 'data'),
                           INDEX_PATH=os.path.join(SITE_ROOT, 'resource/whoosh_index')
                           ))

    app.config.from_envvar('GEEKS_SETTINGS', silent=True)
    app.config.from_object(__name__)

    app.secret_key = 'com.geeksaga.archive'

    return app