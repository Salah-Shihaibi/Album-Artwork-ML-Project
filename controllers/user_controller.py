from flask_restful import Resource
from flask import jsonify, make_response, abort, request
import json
from models.user_model import register_user, login_user

class Register(Resource):
    def post(self):
        print(request.json)
        user =  {'user':register_user(request.json)}
        return user, 200

class Login(Resource):
    def post(self):
        print(request.json, "CONTROLLER")
        cred = {'user':login_user(request.json)} 
        print(cred)
        return cred, 200

class Admin_users(Resource):
    def get(self):        
        return make_response(jsonify({'body': 'You are an admin'}), 200)
