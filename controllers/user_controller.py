from email.mime import application
from flask_restful import Resource
from flask import jsonify, make_response, Response, abort

class Users(Resource):
    def get(self):
        return 200

class Admin_users(Resource):
    def get(self):        
        return make_response(jsonify({'body': 'You are an admin'}), 200)