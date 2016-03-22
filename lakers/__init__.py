# coding=utf-8

from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

import app_settings

template_folder = 'templates'
static_folder = 'static'
if hasattr(app_settings, 'TEMPLATE_FOLDER'):
    template_folder = app_settings.TEMPLATE_FOLDER
if hasattr(app_settings, 'STATIC_FOLDER'):
    static_folder = app_settings.STATIC_FOLDER

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)


app.config.from_object(app_settings)
# app.config.from_pyfile('app_settings.py')

db = SQLAlchemy(app)

from lakers import urls

app.config.from_object(urls)

from lakers.ext.restful import RESTful
from lakers.ext.middleware import MiddleWare

restful = RESTful(app)
middleware = MiddleWare(app)

# app.add_url_rule('/', view_func=home.views.Home.as_view('/'), methods=['GET'])
# app.add_url_rule('/login/', view_func=home.views.LoginView.as_view('/login/'), methods=['GET'])
# app.add_url_rule('/handsome/', view_func=handsome.views.HandSomeAPI.as_view('/handsome/'), methods=['GET'])


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")

@app.errorhandler(500)
def error_page(error):
    return render_template("500.html")

@app.context_processor
def template_processor():
    static_prefix =  app.config.get('STATIC_PREFIX', '')
    return dict(static_prefix=static_prefix)


from lakers.views.webs.los_angeles import views
