from flask import Flask

app = Flask(__name__)

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