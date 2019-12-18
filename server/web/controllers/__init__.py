from .users_controller import Users_ratings_controller
from .users_controller import Users_scores_controller


def init_controllers():
    controllers = {}
    controllers['Users_ratings'] = Users_ratings_controller()
    controllers['Users_scores'] = Users_scores_controller()

    return controllers
