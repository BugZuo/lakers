# -*- coding=utf-8 -*-

from lakers.views import handsome
from lakers.views import home

URLS = (
    ('/api/handsome/', ['GET'], handsome.views.HandSomeAPI), 
    ('/register/', 'POST', home.views.RegisterView),   
)