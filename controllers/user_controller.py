from flask_restful import Resource
from flask import jsonify, make_response, abort, request
from error_handling.error_classes import EmailInvalidError, PasswordTooShortError, EmailTakenError, UsernameTakenError
# from error_handling.error_classes import PasswordTooShortError
from models.user_model import register_user, login_user
from utils.email_verification import is_valid_email
from utils.psql_utils import get_user_column
import psycopg2
from psycopg2 import Error
from error_handling.error_classes import IncorrectRequestBody

class Ping(Resource):
    def get(self):
        return 200

class Register(Resource):
    def post(self):
        try:
            user_data = request.json
            if len(user_data['password']) < 5:
                raise PasswordTooShortError
            if not is_valid_email(user_data['email']):
                raise EmailInvalidError
            if  len(get_user_column('email', user_data["email"])) == 1:
                raise EmailTakenError
            if  len(get_user_column('username', user_data["username"])) == 1:
                raise UsernameTakenError   
            new_user =  {'user':register_user(user_data)}
            return new_user, 200
        except (Exception) as error:
            print(error, "<<<<<<<<<<")
            return error.response()
        except (psycopg2.Error) as error:
            return error

 


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
