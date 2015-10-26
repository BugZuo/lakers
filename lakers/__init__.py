from flask import Flask
import app_settings

template_folder = 'templates'
if hasattr(app_settings, 'TEMPLATE_FOLDER'):
    template_folder = app_settings.TEMPLATE_FOLDER

app = Flask(__name__, template_folder=template_folder)

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