# -*- coding=utf-8 -*-

from lakers.views.apis import handsome
from lakers.views.apis import home

URLS = (
    ('/api/handsome/', ['GET'], handsome.HandSomeAPI),
    ('/register/', 'POST', home.RegisterAPI),
    ('/api/login/', 'POST', home.LoginAPI),
    ('/api/logout/', 'GET', home.LoginAPI),
)
