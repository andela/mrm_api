import os

from app import create_app
from flask_graphql import GraphQLView


config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app(config_name)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()
