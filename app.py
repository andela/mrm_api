from flask import Flask, render_template
from flask_graphql import GraphQLView


from config import config
from helpers.database import db_session
from schema import schema
from healthcheck import HealthCheck
import os
import json


health = HealthCheck()


def postgres_up():
    output = os.system("pg_isready -q")
    return True, output


health.add_check(postgres_up)


def status():
    health.add_check(postgres_up)
    r = health.run()
    x = json.loads(r[0])
    i = x['results'][0]['output']
    return render_template('status.html', output=i)


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.add_url_rule(
        '/mrm',
        view_func=GraphQLView.as_view(
            'mrm',
            schema=schema,
            graphiql=True   # for having the GraphiQL interface
        )
    )
    app.add_url_rule(
        '/healthcheck',
        view_func=lambda: status(),
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
