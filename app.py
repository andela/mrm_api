from flask import Flask, render_template, Response
from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_json import FlaskJSON
from bugsnag.flask import handle_exceptions

from flask_mail import Mail
from config import config
from helpers.database import db_session
from schema import schema
from healthcheck_schema import healthcheck_schema
from helpers.auth.authentication import Auth
from utilities.file_reader import read_log_file

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    FlaskJSON(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)
    handle_exceptions(app)

    @app.route("/", methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route("/logs", methods=['GET'])
    @Auth.user_roles('Super Admin', 'REST')
    def logs():
        response = None
        log_file = 'mrm.err.log'
        try:
            open(log_file)  # trigger opening of file
            response = Response(read_log_file(log_file), mimetype='text')
        except FileNotFoundError:  # pragma: no cover
            message = 'Log file was not found'
            response = Response(message, mimetype='text', status=404)
        return response

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

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
