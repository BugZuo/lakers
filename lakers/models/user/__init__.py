# coding=utf-8

from lakers import db

from datetime import datetime

from lakers.common import utils

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    password = db.Column(db.String(128))
    email = db.Column(db.String(75))
    telephone = db.Column(db.String(15))
    is_staff = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean)
    is_superuser = db.Column(db.Boolean)
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    last_login_time = db.Column(db.DateTime)

    def __init__(self, username, first_name, last_name, password, email, telephone='', is_staff=False, is_active=False, created_at=None, last_login_time=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.telephone = telephone
        self.is_staff = is_staff
        self.is_active = is_active
        self.is_superuser = False
        self.status = 0
        if created_at is None:
            created_at = datetime.utcnow()
        self.created_at = created_at
        if last_login_time is None:
            last_login_time = datetime.utcnow()
        self.last_login_time = last_login_time

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        data = {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'telephone': self.telephone,
            'is_staff': self.is_staff,
            'is_active': self.is_active,
            'is_superuser': self.is_superuser,
            'status': self.status,
            'created_at': utils.standard_time_str(self.created_at),
            'last_login_time': utils.standard_time_str(self.last_login_time),
        }
        return data