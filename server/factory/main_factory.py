from flask import Flask
from flask_restful import Api
from controllers.user_controller import (
    Register,
    Login,
    Ping,
    Secret,
    Super_secret,
    Manage_User_Access,
    Pong,
)


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Ping, "/")
    api.add_resource(Pong, "/pong")
    api.add_resource(Register, "/auth/register")
    api.add_resource(Login, "/auth/login")
    api.add_resource(Secret, "/secret")
    api.add_resource(Super_secret, "/superSecret")
    api.add_resource(Manage_User_Access, "/manage_user_access")
    if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0", port=8080)
    return app
