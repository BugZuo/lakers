# -*- coding=utf-8 -*-

from lakers.views.webs import home
from lakers.views.webs import handsome

URLS = (
    ('/', ['GET'], home.views.Home),
    ('/login/', ['GET', 'POST'], home.views.LoginView),
    ('/handsome/', ['GET'], handsome.views.HandSomeView),
    ('/register/', 'GET', home.views.RegisterView),
)