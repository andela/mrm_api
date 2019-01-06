from flask import Flask, render_template

from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_json import FlaskJSON
from flask_socketio import SocketIO
from flask_executor import Executor

from flask_mail import Mail
from config import config
from helpers.database import db_session
from schema import schema
from healthcheck_schema import healthcheck_schema
from helpers.auth.authentication import Auth
from helpers.socket.socketio import Namespaceio
from helpers.socket.background_thread import req_thread
from api.analytics.analytics_request import AnalyticsRequest

async_mode = None

executor = Executor()
socketio = SocketIO()
mail = Mail()


def create_app(config_name):  # noqa: C901
    app = Flask(__name__)
    CORS(app)
    FlaskJSON(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)
    socketio.init_app(app)
    executor.init_app(app)

    background_thread = lambda status=False: req_thread(socketio, status)  # noqa : E731

    @app.route('/')
    def index():
        return render_template('index.html', async_mode=socketio.async_mode)

    socketio.on_namespace(
        Namespaceio(
            '/io', background_thread=background_thread, socketio=socketio))

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

    def analytic_respond():
        return AnalyticsRequest.validate_request(AnalyticsRequest)

    @app.route("/analytics", methods=['POST'])
    @Auth.user_roles('Admin', 'REST')
    def analytics_report():
        future = executor.submit(analytic_respond)
        while future.running():
            background_thread(status=future.running())
        return future.result()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
