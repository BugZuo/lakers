# coding=utf-8

from flask import Flask
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

restful = RESTful(app)

# app.add_url_rule('/', view_func=home.views.Home.as_view('/'), methods=['GET'])
# app.add_url_rule('/login/', view_func=home.views.LoginView.as_view('/login/'), methods=['GET'])
# app.add_url_rule('/handsome/', view_func=handsome.views.HandSomeAPI.as_view('/handsome/'), methods=['GET'])


@app.errorhandler(404)
def not_found(error):
	return "404!"

from lakers.views.los_angeles import views
