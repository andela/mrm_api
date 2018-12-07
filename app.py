from flask import Flask, render_template

from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_json import FlaskJSON
from flask_socketio import SocketIO
from threading import Lock

from flask_mail import Mail
from config import config
from helpers.database import db_session
from schema import schema
from healthcheck_schema import healthcheck_schema
from helpers.auth.authentication import Auth
from api.analytics.analytics_request import AnalyticsRequest

async_mode = None

mail = Mail()
socketio = SocketIO()
thread = None
thread_lock = Lock()





def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    FlaskJSON(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)
    socketio.init_app(app,  path='/socket.io', async_mode=async_mode)

    def background_thread():
        """Example of how to send server generated events to clients."""
        count = 0
        while True:
            socketio.sleep(10)
            count += 1
            socketio.emit('my_response',
                        {'data': 'Server generated event', 'count': count},
                        namespace='/test')


    @app.route("/")
    def index():
        return render_template('index.html', async_mode=socketio.async_mode)

    @socketio.on('my_event', namespace='/test')
    def testc_message(message):
        # session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
            {'data': message['data'], 'count': 1})

    @socketio.on('connect', namespace='/test')
    def testc_connect():
        global thread
        with thread_lock:
            if thread is None:
                thread = socketio.start_background_task(background_thread)
        emit('my_response', {'data': 'Connected', 'count': 0})



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
