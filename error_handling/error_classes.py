from flask import make_response, abort, jsonify
from flask_restful import Resource

class CustomError(Exception):
    def __init__(self):
        self.msg = 'Internal server error.'
        self.status = 500
    def response(self):
        return {
            "msg": self.msg,
            "status": self.status
        }, self.status 

class PasswordTooShortError(CustomError):
    def __init__(self):        
        self.msg = 'Password should be 5 characters or longer.'
        self.status = 400

class UsernameTakenError(CustomError):
    def __init__(self):      
        self.msg = 'Username is already in use.'
        self.status = 400

class EmailTakenError(CustomError):
    def __init__(self):
        self.msg = 'Email address is already in use.'
        self.status = 400

class EmailInvalidError(CustomError):
    def __init__(self):
        self.msg = 'Email address invalid.'
        self.status = 400




