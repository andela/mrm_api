from flask import Flask
from flask_graphql import GraphQLView


from config import config
from helpers.database import db_session
from schema import schema
from helpers.auth.decode_token import Auth


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.add_url_rule(
        '/mrm',
        view_func=GraphQLView.as_view(
            'mrm',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    def graphql_view():
        view = GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
            )
        return Auth.auth_required(view)
    

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
    return app
