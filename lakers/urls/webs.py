# -*- coding=utf-8 -*-

from lakers.views.webs import home
from lakers.views.webs import handsome

URLS = (
    ('/', ['GET'], home.views.Home),
    ('/login/', ['GET', 'POST'], home.views.LoginView),
    ('/register/', 'GET', home.views.RegisterView),

    ('/handsome/', ['GET'], handsome.views.HandSomeView),
    ('/post/', ['GET'], handsome.views.PostHtmlView),
)