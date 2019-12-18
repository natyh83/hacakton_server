from ..models.users_model import Users_model

class Users_service():

    def __init__(self):
        self.user_model = Users_model()

    def get_user_ratings(self, user_id):
        print(user_id)
        user_ratings = self.user_model.get_user_ratings_by_id(str(user_id))

        return user_ratings

    def get_user_engagement(self, user_id):
        print(user_id)
        return self.user_model.get_user_engagement_by_id(str(user_id))

