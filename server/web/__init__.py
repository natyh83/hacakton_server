from flask import Flask
from .error_handler import handle_exception


def init_app():
    app = Flask(__name__)
    # app.register_error_handler(Exception, handle_exception)

    # Enable cross origin access
    # CORS(app)

    app.run
    return app


def add_routes(api, controllers):
    api.add_resource(controllers['users'], "/api/user/<customer_id>", endpoint="Users_controller")
    return api
