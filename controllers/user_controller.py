from flask_restful import Resource
from flask import request
from error_handling.error_classes import (
    EmailInvalidError,
    PasswordTooShortError,
    EmailTakenError,
    UsernameTakenError,
    IncorrectRequestBodyError,
    CustomError,
)
from models.user_model import register_user, login_user
from utils.email_verification import is_valid_email
from utils.psql_utils import get_user_column


class Ping(Resource):
    @staticmethod
    def get():
        return 200


class Register(Resource):
    @staticmethod
    def post():
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
        except CustomError as error:
            return error.response()


class Login(Resource):
    @staticmethod
    def post():

        try:
            if "email" in request.json and "password" in request.json:
                if not isinstance(request.json["email"], str) or not isinstance(
                    request.json["password"], str
                ):
                    raise IncorrectRequestBodyError
            else:
                raise IncorrectRequestBodyError

            cred = {"user": login_user(request.json)}
            return cred, 200
        except CustomError as error:
            return error.response()
