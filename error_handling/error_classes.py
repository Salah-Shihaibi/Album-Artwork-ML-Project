# does body contain correct dictionary format

# handle psql error

## email address incorrect format, 
# username already in use, 
# email address already in use
# password not long enough
from flask import make_response, abort, jsonify
from flask_restful import Resource


class UsernameTakenError(Exception):
    abort(make_response(jsonify({
        "status":400,
        "msg":'Username already exists.'
        })), 400)

class EmailTakenError(Exception):
    abort(make_response(jsonify({
        "status":400,
        "msg":'Email already exists.'
        })), 400)

class PasswordTooShortError(Exception):
    abort(make_response(jsonify({
        "status":400,
        "msg":'Password should be 5 characters or longer.'
        })),400)


