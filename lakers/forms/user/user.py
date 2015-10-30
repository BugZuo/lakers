# coding=utf-8

__author__ = 'bug'


from wtforms.form import Form
from wtforms import StringField, validators

class RegisterForm(Form):
    username = StringField(label=u'username', validators=[validators.DataRequired()])
    first_name = StringField(label=u'first_name', validators=[validators.DataRequired()])
    last_name = StringField(label=u'last_name', validators=[validators.DataRequired()])
    email = StringField(label=u'email', validators=[validators.DataRequired()])
    telephone = StringField(label=u'telephone')
    password = StringField(label=u'password', validators=[validators.DataRequired()])
    repeat_password = StringField(label=u'repeat_password', validators=[validators.DataRequired()])