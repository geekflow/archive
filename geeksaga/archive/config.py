#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    .config
    ~~~~~~~~

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""
import os

class Config(object):
    SITE_ROOT = os.path.abspath(os.path.dirname(__file__))
    DB_FILE_PATH= 'resource/database/archive.db'
    DB_URL= 'sqlite:///' + os.path.join(SITE_ROOT, DB_FILE_PATH)
    TMP_FOLDER = 'resource/tmp/'
    UPLOAD_FOLDER = 'resource/upload/'
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    PERMANENT_SESSION_LIFETIME = 60 * 60
    SESSION_COOKIE_NAME = 'geeksaga_archive_session'
    LOG_LEVEL = 'debug'
    LOG_FILE_PATH = 'resource/log/archive.log'
    DB_LOG_FLAG = 'True'
    ARCHIVE_PATH = os.path.join(SITE_ROOT, 'data')
    ARCHIVE_BACKUP_PATH = os.path.join(SITE_ROOT, 'data_backup')
    INDEX_PATH = os.path.join(SITE_ROOT, 'resource/whoosh_index')