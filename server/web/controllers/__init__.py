from .users_controller import Users_controller


def init_controllers():
    controllers = {}
    controllers['users'] = Users_controller()

    return controllers
