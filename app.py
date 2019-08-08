import os
from flask import Flask, render_template
from flask_graphql import GraphQLView
from flask_json import FlaskJSON

from flask_mail import Mail
from config import config
from helpers.database import db_session
from schema import schema
from flask_cors import CORS
from healthcheck_schema import healthcheck_schema
from helpers.auth.authentication import Auth
from helpers.auth.allowed_requests import validate_origins
from api.analytics.analytics_request import AnalyticsRequest

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    FlaskJSON(app)
    if config_name == 'development' or 'testing':
        CORS(app, resources={r"/mrm": {"origins": "*"}})
    if config_name == 'production':
        CORS(app, resources={
            r"/mrm": {"origins": os.environ.get("PROD_REQUEST_URL").split(',')}})  # noqa 501

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)

    @app.route("/", methods=['GET'])
    def index():
        return render_template('index.html')

    app.add_url_rule(
        '/mrm',
        view_func=GraphQLView.as_view(
            'mrm',
            schema=schema,
            graphiql=True   # for having the GraphiQL interface
        )
    )

    app.before_request(validate_origins)

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
