#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
     Created on 2014. 8. 24.

     @author: geeksaga
     :copyright: (c) 2014 by geeksaga.
     :license: MIT LICENSE 2.0, see license for more details.
'''

import os
from whoosh.index import create_in
from whoosh.qparser import QueryParser
from whoosh.fields import *

class ArchiveSearch(object):
    def __init__(self, index_path):
        self.index_path = index_path 
        if not os.path.exists(self.index_path):
            os.makedirs(self.index_path)
            
        self.schema = Schema(path=ID(stored=True), content=TEXT, tags=NGRAMWORDS(stored=True))
        self.whoosh = create_in(self.index_path, self.schema)
        self.writer = self.whoosh.writer()
    
    def add(self, path, content, tags):
        self.writer.add_document(path=path, content=content, tags=tags)
        self.writer.commit()
        
    def search(self, field, query):
        with self.whoosh.searcher() as searcher:
            query = QueryParser(field, self.schema).parse(query)
            result = searcher.search(query)
            for r in result:
                print(r)