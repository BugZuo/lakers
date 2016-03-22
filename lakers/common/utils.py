# coding=utf-8

import sys
import os

cur_dir = os.path.abspath(__file__)
sys.path.insert(0, '/'.join(cur_dir.split('/')[:-3]))

from datetime import datetime

import hashlib
from lakers.app_settings import APP_TIMEZONE

__author__ = 'bug'

STANDARD_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

SALT = 'flyzfq'

def standard_time_str(t):
    if t is None or not isinstance(t, datetime):
        return datetime.now(tz=APP_TIMEZONE).strftime(STANDARD_TIME_FORMAT)
    return t.strftime(STANDARD_TIME_FORMAT)

def create_password(password):
    password = str(password)
    sha1 = hashlib.sha1()
    sha1.update(SALT + password)
    return "%s$%s" % (sha1.hexdigest(), SALT)

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