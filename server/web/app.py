from flask_restful import Api

from server.web import init_app
from server.web import add_routes
from server.web.controllers import init_controllers

controllers = init_controllers()

# Init app and db
app = init_app()
app.app_context().push()

# Add resources and routes
api = Api(app)
api = add_routes(api, controllers)


# Test resource
# api.add_resource(Test, "/api/test/<id>")

# Raise flask exception instead of flask-restful exception
def raise_exception(sender, exception, **extra):
    raise exception


from flask_restful import got_request_exception

got_request_exception.connect(raise_exception, app)

app.run()
