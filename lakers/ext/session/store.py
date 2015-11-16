# coding=utf-8

__author__ = 'bug'

import time
import json
import base64
try:
    import cPickle as pickle
except ImportError:
    import pickle

from lakers import app_settings as settings
from lakers.config.redis_conf import session_server
from .base import SessionBase, CreateError

class SessionStore(SessionBase):

    """
    Implements Redis database session store.
    """
    PLATFORM_SESSION = {'BIND_SITES', '_auth_user_id', 'album_freq'}
    def __init__(self, session_key=None):
        super(SessionStore, self).__init__(session_key)
        self.server = session_server
        if not session_key:
            self.create()
        self._saved = False

    def load(self):
        # start_time = time.time()
        session_data = self.server.get(self.session_key)
        obj = self.decode(session_data)
        # end_time = time.time()
        # exe_time = start_time - end_time
        return obj

    def exists(self, session_key):
        if self.server.get(session_key):
            return True
        return False

    def create(self):
        while True:
            self.session_key = self._get_new_session_key()
            try:
                self.save( must_create=True)
            except CreateError:
                continue
            self.modified = True
            return

    def save(self, must_create=False, is_login=False):
        if must_create and self.exists(self.session_key):
            raise CreateError
        data = self.encode(self.get_session(no_load=must_create))
        if is_login:
            expires = settings.SESSION_COOKIE_AGE_LOGIN_USER
        else:
            expires = self.get_expiry_age()
        self.server.set(self.session_key, data)
        self.server.expire(self.session_key, expires)

    def delete(self, session_key=None):
        if session_key is None:
            if self._session_key is None:
                return
            session_key = self._session_key

        try:
            self.server.delete(session_key)
        except:
            pass

    # new format:
    # hashcode:${pickled_session_dict}:${optional_json_session_dict}
    def encode(self, session_dict):
        session_str = json.dumps(session_dict)
        hash_id = self._hash(session_str)
        return ':'.join([base64.encodestring(hash_id), session_str])

    def decode(self, session_data):
        if not session_data:
            return {}
        ret = None
        try:
            hash_value, json_session = session_data.split(':', 1)
            '''
            expected_hash = self._hash(json_session)
            if not constant_time_compare(base64.decodestring(hashv),
                                         expected_hash):
                raise ValueError("Session data corrupted")
            '''
            ret = json.loads(json_session)
        except Exception as e:
            return {}
        return ret

