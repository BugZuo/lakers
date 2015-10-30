# coding=utf-8

__author__ = 'bug'

from wtforms.form import Form
from wtforms import StringField, validators

class LoginForm(Form):
    username = StringField(label=u'username', validators=[validators.DataRequired()])
    password = StringField(label=u'password', validators=[validators.DataRequired()])
