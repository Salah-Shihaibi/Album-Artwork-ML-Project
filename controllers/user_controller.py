from flask_restful import Resource
from flask import request
from error_handling.error_classes import (
    EmailInvalidError,
    PasswordTooShortError,
    EmailTakenError,
    UsernameTakenError,
    IncorrectRequestBodyError,
)
from models.user_model import register_user, login_user
from utils.email_verification import is_valid_email
from utils.psql_utils import get_user_column
import psycopg2


class Ping(Resource):
    def get(self):
        return 200


class Register(Resource):
    def post(self):
        try:
            user_data = request.json
            if (
                not "email" in request.json
                or not "password" in request.json
                or not "username" in request.json
                or not "name" in request.json
            ):
                raise IncorrectRequestBodyError
            if len(user_data["password"]) < 5:
                raise PasswordTooShortError
            if not is_valid_email(user_data["email"]):
                raise EmailInvalidError
            if len(get_user_column("email", user_data["email"])) == 1:
                raise EmailTakenError
            if len(get_user_column("username", user_data["username"])) == 1:
                raise UsernameTakenError
            new_user = {"user": register_user(user_data)}
            return new_user, 200
        except (Exception, psycopg2.Error) as error:
            return error.response()


class Login(Resource):
    def post(self):
        try:
            if "email" in request.json and "password" in request.json:
                if type(request.json["email"] and request.json["password"]) != str:
                    raise IncorrectRequestBodyError
            else:
                raise IncorrectRequestBodyError

            cred = {"user": login_user(request.json)}
            return cred, 200
        except Exception as err:
            return err.response()
