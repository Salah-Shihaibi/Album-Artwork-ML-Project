from flask_restful import Resource
from flask import jsonify, make_response, abort, request
from error_handling.error_classes import PasswordTooShortError
# from error_handling.error_classes import PasswordTooShortError
from models.user_model import register_user, login_user
from error_handling.error_classes import IncorrectRequestBody

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
        try:
            if "email" in request.json and "password" in request.json:
                if type(request.json["email"] and request.json["password"]) != str:
                    raise IncorrectRequestBody
            else:
                raise IncorrectRequestBody
                
            cred = {'user':login_user(request.json)} 
            print(cred, "im not an error <<<<<<")
            return cred, 200
        except Exception as err:
            print("im an error", err.response())
            return err.response()
