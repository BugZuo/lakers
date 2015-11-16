# coding=utf-8

import pytz

from datetime import datetime

import hashlib
import sys

from lakers.app_settings import APP_TIMEZONE

__author__ = 'bug'

STANDARD_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

SALT = 'lakers'

def standard_time_str(t):
    if t is None or not isinstance(t, datetime):
        return datetime.now(tz=APP_TIMEZONE).strftime(STANDARD_TIME_FORMAT)
    return t.strftime(STANDARD_TIME_FORMAT)

def create_password(password):
    password = str(password)
    md5 = hashlib.md5()
    md5.update(password + "$" + SALT)
    return md5.hexdigest()

def to_bytes(x, charset=sys.getdefaultencoding(), errors='strict'):
    if x is None:
        return None
    if isinstance(x, (bytes, bytearray, buffer)):
        return bytes(x)
    if isinstance(x, unicode):
        return x.encode(charset, errors)
    raise TypeError('Expected bytes')

if __name__=='__main__':
    print create_password('asd')