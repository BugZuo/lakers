# -*- coding=utf-8 -*-

from flask import request, make_response
from lakers import app_settings as settings
from lakers.services.user.manage import user_core_service


class CookieMiddleWare(object):
    @staticmethod
    def main(response=None):
        """
        If request.session was modified, or if the configuration is to save the
        session every time, save the changes and set a session cookie.
        """
        if response is None:
            return
        else:
            try:
                accessed = request.session.accessed
                modified = request.session.modified
            except AttributeError:
                pass
            else:
                if modified or settings.SESSION_SAVE_EVERY_REQUEST:

                    # Save the session data and refresh the client cookie.
                    is_login = request.user is not None
                    request.session.save(is_login=is_login)
                    if request.session.get_expire_at_browser_close():
                        max_age = -1
                    else:
                        max_age = request.session.get_expiry_age()
                    response.set_cookie(settings.SESSION_COOKIE_NAME,
                                        value=request.session.session_key,
                                        max_age=max_age,
                                        # domain=settings.SESSION_COOKIE_DOMAIN,
                                        path=settings.SESSION_COOKIE_PATH,
                                        secure=settings.SESSION_COOKIE_SECURE or False,
                                        httponly=settings.SESSION_COOKIE_HTTPONLY or False)
            return response
