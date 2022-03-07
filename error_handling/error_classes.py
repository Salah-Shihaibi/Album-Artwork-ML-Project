# handle psql error

from flask import make_response, abort, jsonify
from flask_restful import Resource

class CustomError(Exception):
    def __init__(self):
        self.msg = 'Internal server error.'
        self.status = 500
    def response(self):
        self.msg = 'Internal server error'
        self.status_code = 500
    def response(self):
        return {"msg":self.msg, "status_code": self.status_code}, self.status_code 

class PasswordTooShortError(CustomError):
    def __new__(self):
        self.msg = 'Password should be 5 characters or longer.'
        self.status = 400
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

# class EmailTakenError(Exception):
#     abort(make_response(jsonify({
#         "status":400,
#         "msg":'Email already exists.'
#         })), 400)

# user does not exist
class NoUserFoundError(CustomError):
    def __init__(self):
        self.msg = 'User/password combination is not valid.' 
        self.status_code = 400

# user exists incorrect password
class IncorrectPasswordError(CustomError):
    def __init__(self):
        self.msg = 'User/password combination is not valid.' 
        self.status_code = 400
        
# incorrect request body
class IncorrectRequestBody(CustomError):
    def __init__(self):
        self.msg = 'Credentials invalid format' 
        self.status_code = 400
        
  

