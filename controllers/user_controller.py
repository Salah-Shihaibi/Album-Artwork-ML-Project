from email.mime import application
from flask_restful import Resource
from flask import jsonify, make_response, Response

class Users(Resource):
    def get(self):
        return 200

class Admin_users(Resource):
    def get(self):        
        return make_response(jsonify({'body': 'You are an admin'}), 200)

    # response = app.response_class(
    #     response=json.dumps(),
    #     mimetype='application/json'
    # )
    # return response