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
    api.add_resource(controllers['Users_ratings'], "/api/user/ratings/<customer_id>", endpoint="Users_ratings_controller")
    api.add_resource(controllers['Users_scores'], "/api/user/score/<customer_id>", endpoint="Users_scores_controller")
    return api
