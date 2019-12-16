from flask import request
from flask_restful import Resource
from flask import jsonify

from ..services.users_service import Users_service


class Users_controller(Resource):

    def __init__(self):
        self.users_service = Users_service()

    def get(self, customer_id):
        print('customer_id:' + customer_id)
        # customer_id = request.form["customer_id"]
        user_ratings = self.users_service.get_user_ratings(customer_id)

        return jsonify(user_ratings)
