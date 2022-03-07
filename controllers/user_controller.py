from flask_restful import Resource
from flask import jsonify, make_response, abort, request
from error_handling.error_classes import PasswordTooShortError
# from error_handling.error_classes import PasswordTooShortError
from models.user_model import register_user, login_user

class Ping(Resource):
    def get(self):
        return 200

class Register(Resource):
    def post(self):
        return PasswordTooShortError()
        # user =  {'user':register_user(request.json)}
        # print(user, type(user), "<<<<<<<<<<<<<")
        # if len(user['password']) < 5:
        # #     raise PasswordTooShortError
        # return user, 200

class Login(Resource):
    def post(self):
        cred = {'user':login_user(request.json)} 
        return cred, 200
