# -*- coding=utf-8 -*-

from flask.views import MethodView
from flask import request, make_response

from lakers.forms.user import RegisterForm
from lakers.forms.login import LoginForm
from lakers.common import api

from lakers.ext.session.manage import store_cookie, save_session

from lakers.services.user import user_core_service

from lakers import app_settings as settings


class RegisterAPI(MethodView):
    def post(self):
        form = RegisterForm(request.form)

        if not form.validate():
            return api.jsn(api.invalid_param, message=form.errors)

        form_data = form.data

        user_by_name = user_core_service.get_by_name(form_data['username'])

        if user_by_name is not None:
            return api.jsn(data="user is existed!")

        user_by_email = user_core_service.get_by_email(form_data['email'])

        if user_by_email is not None:
            return api.jsn(data="email is existed!")

        result = user_core_service.add(form_data)

        if result:
            return api.jsn(status=api.success, data="register success!")
        else:
            return api.jsn(status=api.inner_error, message="error happened!")


class LoginAPI(MethodView):
    def post(self):
        form = LoginForm(request.form)

        if not form.validate():
            return api.jsn(status=api.invalid_param, message=form.errors)

        user = user_core_service.validate_user(form.data)

        if user is None:
            return api.jsn(status=api.invalid_param, message="error username or password")

        user = user.serialize()
        data = {
            'user': user,
        }
        response = make_response(api.jsn(api.success, data=data))
        save_session(user['id'], user['username'])
        return store_cookie(response, user['id'])

    def get(self):
        request.session.set_expiry(0)
        request.session.flush()
        response = make_response(api.jsn(api.success))
        response.set_cookie(settings.SESSION_USER_ID_KEY, max_age=-1)
        return response

