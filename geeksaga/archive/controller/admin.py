# -*- coding: utf-8 -*-
"""
    admin page
    ~~~~~~~~~

    writing module for markdown format similar wiki.

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from flask import render_template
from ..blueprint import frontend
from ..decorator import login_required

import zipfile
from datetime import datetime
from os import mkdir, walk
from os.path import join, exists, splitext

from .ArchiveAPI import archive_list, archive_attach_list

@frontend.record
def record(setup_state):
    global archive_path, archive_attach_path, archive_back_path, app
    app = setup_state.app
    archive_path = app.config.get('ARCHIVE_PATH')
    archive_attach_path = join(archive_path, 'attach')
    archive_back_path = app.config.get('ARCHIVE_BACKUP_PATH')
    
@frontend.route('/admin/data/backup')
@login_required
def data_backup():
    if not exists(archive_back_path):
        mkdir(archive_back_path, 755)
    
    try:
        import zlib
        compression = zipfile.ZIP_DEFLATED
    except:
        compression = zipfile.ZIP_STORED
        
    with zipfile.ZipFile(backup_filename(), mode='w') as zf:
        for file in archive_list():
            zf.write(join(archive_path, file + '.md'), arcname=file + '.md', compress_type=compression)
            
        for file in archive_attach_list():
            zf.write(join(archive_attach_path, file), arcname=file, compress_type=compression)
            
        print(zf.namelist())
        
    return ''

@frontend.route('/admin/backup/list', methods=['GET'])
@login_required
def backup_list():
    return render_template('admin/list.html', entries=backup_files())

def backup_files():
    file_paths = []

    for (dirpath, dirnames, filenames) in walk(archive_back_path):
        for filename in filenames:
            if splitext(filename)[1].lower() == '.zip':
                file_paths.append(join(dirpath, filename)[len(archive_back_path) + 1:])
                
    return file_paths

def backup_filename():
    return join(archive_back_path, 'archive-' + now() + '.zip')

def now():
    return datetime.now().strftime("%Y%m%d%H")

if __name__ == '__main__':
    try:
        print(now())
        data_backup()
    except KeyboardInterrupt as e:
        pass
