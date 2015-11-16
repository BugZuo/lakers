# coding=utf-8

from lakers.models import User

from lakers import db

from lakers.common import utils

from flask import logging

logger = logging.getLogger("user")

class UserCoreService(object):
    def get_by_id(self, id):
        user = User.query.filter_by(id=id).first()
        return user

    def get_by_name(self, username):
        user = User.query.filter_by(username=username).first()
        return user
    def get_by_email(self, email):
        user = User.query.filter_by(email=email).first()
        return user

    def add(self, form_data):
        user = User(form_data['username'], form_data['first_name'], form_data['last_name'],
                    utils.create_password(form_data['password']), form_data['email'])
        try:
            db.session.add(user)
            db.session.commit()
            return True
        except Exception, e:
            logger.error(e)
            return False

    def validate_user(self, form_data):
        return User.query.filter_by(username=form_data['username'], password=utils.create_password(form_data['password'])).first()

user_core_service = UserCoreService()