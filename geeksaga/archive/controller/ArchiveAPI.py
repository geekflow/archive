# -*- coding: utf-8 -*-
"""
    ArchiveAPI
    ~~~~~~~~~

    writing module for markdown syntax format similar wiki.

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from flask import session, redirect, request, url_for
from flask import render_template, send_file
from flask.views import MethodView

from ..blueprint import frontend
from ..decorator import login_required, templated, user_required
from ..model import search
from ..util import md

from os import sep, mkdir, walk
from os.path import join, splitext, isdir, exists

class ArchiveAPI(MethodView):
    decorators = [user_required]

    @templated('archive/create.html')
    def get(self):
        print('ArchiveAPI GET')
        return dict(page=request.args['page'] or None)

    def post(self):
        print('ArchiveAPI POST')
        pass

    def delete(self, user_id):
        print('ArchiveAPI DELETE')
        pass

    def put(self, page=None):
        print('ArchiveAPI put')
        pass

@frontend.record
def record(setup_state):
    global archive_path, index_path, app
    app = setup_state.app
    archive_path = app.config.get('ARCHIVE_PATH')
    index_path = app.config.get('INDEX_PATH')

@frontend.route('/archive', methods=['POST'])
@login_required
def add():
    if request.form['page']:
        page = request.form['page'].replace(':', '/')
        path = page[:page.rfind('/')]

        full_path = join(archive_path, path)

        if not isdir(full_path):
            mkdir(full_path, 755)
    
        if session.get('user_info'):
            content = request.form['content']
            full_path = join(archive_path, page + '.md')
            
            print(request.form)
            
            with open(full_path, 'w+', encoding='utf-8') as f:
                f.write(content)

            archiveSearch = search.ArchiveSearch(index_path)
            archiveSearch.add(path=page + '.md', content=content, tags='')
            archiveSearch.search('content', 'TEST')
                        
            return redirect(url_for('.read', page=page))
    
    return "fail"
    
@frontend.route('/archive/read/<path:page>', methods=['GET'])
def read(page=None):
    if(page.startswith('attach/')):
        return redirect(url_for('.attach', filename=page))
    
    full_path = join(archive_path, page + '.md')
    
    if not exists(full_path):
        return redirect(url_for('archive_api', page=page))
    
    return render_template('archive/read.html', archive=archive_read(full_path, True))

@frontend.route('/archive/attach/<path:filename>', methods=['GET'])
def attach(filename=None):
    return send_file(join(archive_path, filename))

@frontend.route('/archive/write/<path>', methods=['POST'])
def write(path):
    if not exists(path):
        return redirect(url_for('archive'))
    return render_template(path + '.html')

@frontend.route('/archive/list', methods=['GET'])
def getList():
    return render_template('archive/list.html', entries=archive_list())

def archive_read(path, isFormat=False):
    if(isFormat):
        return md.convert(open(path, 'r', encoding='utf-8').read())
    else:
        return open(path, 'r', encoding='utf-8').read()

def archive_list():
    file_paths = []

    #onlyfiles = [ f for f in listdir(archive_path) if isfile(join(archive_path, f)) ]

    for (dirpath, dirnames, filenames) in walk(archive_path):
        #directories[:] = [dir for dir in directories if dir != ".git"]
        
        for filename in filenames:
            if splitext(filename)[1].lower() == '.md':
                file_paths.append(join(dirpath, filename)[len(archive_path) + 1:].rstrip('.md').replace(sep, '/'))
                
    return file_paths

def archive_attach_list():
    file_paths = []

    archie_attach_path = join(archive_path, 'attach')

    for (dirpath, dirnames, filenames) in walk(archie_attach_path):
        for filename in filenames:
            file_paths.append(join(dirpath, filename)[len(archie_attach_path) + 1:])
                
    return file_paths