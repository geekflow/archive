# -*- coding: utf-8 -*-
"""
    .i18n
    ~~~~~~~~~

    writing module for markdown syntax format similar wiki.

    :copyright: (c) 2014 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

import gettext
from gettext import gettext as _

gettext.bindtextdomain('archive', 'resource/i18n')
gettext.textdomain('archive')

#t = gettext.translation('archive', 'resource/i18n', fallback = True)
    
print(_('This message is in the script.'))