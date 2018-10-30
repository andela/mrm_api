from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_json import FlaskJSON
from helpers.auth.authentication import Auth

from flask_mail import Mail
from config import config
from helpers.database import db_session
from schema import schema
from healthcheck_schema import healthcheck_schema
from api.analytics.analytics_request import AnalyticsRequest

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    FlaskJSON(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)

    app.add_url_rule(
        '/mrm',
        view_func=GraphQLView.as_view(
            'mrm',
            schema=schema,
            graphiql=True   # for having the GraphiQL interface
        )
    )
    app.add_url_rule(
        '/_healthcheck',
        view_func=GraphQLView.as_view(
            '_healthcheck',
            schema=healthcheck_schema,
            graphiql=True   # for healthchecks
        )
    )

    @app.route("/analytics", methods=['POST'])
    @Auth.user_roles('Admin', 'REST')
    def analytics_report():
        return AnalyticsRequest.validate_request(AnalyticsRequest)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
