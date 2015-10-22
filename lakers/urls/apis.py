# -*- coding=utf-8 -*-

from lakers.views import handsome

URLS = (
    ('/api/handsome/', ['GET'], handsome.views.HandSomeAPI),    
)