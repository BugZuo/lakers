# coding=utf-8

from flask import jsonify

class API(object):

    success = 1
    not_login = 2
    invalid_request = 3
    invalid_param = 4
    inner_error = 5
    unknown = 6

    @staticmethod
    def jsn(status=1, message=None, data=None, *args, **kw):
        result = {
            "status": status,
            "success": status == 1,
            }
        if data is not None:
            result['data'] = data
        if message is not None:
            result['message'] = message
        return jsonify(result)

api = API()