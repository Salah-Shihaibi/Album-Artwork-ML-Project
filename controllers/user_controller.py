from flask_restful import Resource
from flask import jsonify, make_response, abort, request
from models.user_model import register_user, login_user

class Ping(Resource):
    def get(self):
        return 200

class Register(Resource):
    def post(self):
        user =  {'user':register_user(request.json)}
        return user, 200

class Login(Resource):
    def post(self):
        cred = {'user':login_user(request.json)} 
        return cred, 200
