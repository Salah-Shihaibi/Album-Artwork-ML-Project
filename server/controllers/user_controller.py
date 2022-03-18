from flask import request
from flask_restful import Resource
from firebase_app import auth, validate_token, validate_access
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


class Pong(Resource):
    @staticmethod
    def get():
        return 201


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


class Secret(Resource):
    @staticmethod
    def get():
        try:
            validate_token(request)
            return {"secret": "I have an identical twin, also called ed"}, 200

        except Exception as err:
            return {"msg": str(err)}, 401


class Super_secret(Resource):
    @staticmethod
    def get():
        try:
            decoded_token = validate_token(request)
            if validate_access(decoded_token):
                return {"access": "granted"}, 200
            return {"access": "NOT granted"}, 401

        except Exception as err:
            return {"msg": str(err)}, 401


# admin: change user claims
class Manage_User_Access(Resource):
    @staticmethod
    def patch():
        try:
            decoded_token = validate_token(request)
            if validate_access(decoded_token):
                auth.set_custom_user_claims(
                    request.json["uid"], {"admin": request.json["admin"]}
                )
                return {}, 204
            return {"msg": "Insufficient permissions"}, 403

        except Exception as err:
            return {"msg": str(err)}, 401


# upload image to trianing set
# admin: begin training