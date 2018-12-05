from string import Template
from flask import Flask, render_template, make_response

from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_json import FlaskJSON
from graphql_ws.gevent import GeventSubscriptionServer
from flask_sockets import Sockets

from flask_mail import Mail
from config import config
from helpers.database import db_session
from schema import schema
from healthcheck_schema import healthcheck_schema
from helpers.auth.authentication import Auth
from api.analytics.analytics_request import AnalyticsRequest

mail = Mail()
socket = Sockets()


def render_graphiql():
    return Template('''
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>GraphiQL</title>
  <meta name="robots" content="noindex" />
  <style>
    html, body {
      height: 100%;
      margin: 0;
      overflow: hidden;
      width: 100%;
    }
  </style>
  <link href="//cdn.jsdelivr.net/npm/graphiql@0.12.0/graphiql.css" rel="stylesheet" />
  <script src="//cdn.jsdelivr.net/fetch/0.9.0/fetch.min.js"></script>
  <script src="//cdn.jsdelivr.net/react/15.0.0/react.min.js"></script>
  <script src="//cdn.jsdelivr.net/react/15.0.0/react-dom.min.js"></script>
  <script src="//cdn.jsdelivr.net/npm/graphiql@0.12.0/graphiql.min.js"></script>
  <script src="//unpkg.com/subscriptions-transport-ws@${SUBSCRIPTIONS_TRANSPORT_VERSION}/browser/client.js"></script>
  <script src="//unpkg.com/graphiql-subscriptions-fetcher@0.0.2/browser/client.js"></script>
</head>
<body>
  <script>
    // Collect the URL parameters
    var parameters = {};
    window.location.search.substr(1).split('&').forEach(function (entry) {
      var eq = entry.indexOf('=');
      if (eq >= 0) {
        parameters[decodeURIComponent(entry.slice(0, eq))] =
          decodeURIComponent(entry.slice(eq + 1));
      }
    });
    // Produce a Location query string from a parameter object.
    function locationQuery(params, location) {
      return (location ? location: '') + '?' + Object.keys(params).map(function (key) {
        return encodeURIComponent(key) + '=' +
          encodeURIComponent(params[key]);
      }).join('&');
    }
    // Derive a fetch URL from the current URL, sans the GraphQL parameters.
    var graphqlParamNames = {
      query: true,
      variables: true,
      operationName: true
    };
    var otherParams = {};
    for (var k in parameters) {
      if (parameters.hasOwnProperty(k) && graphqlParamNames[k] !== true) {
        otherParams[k] = parameters[k];
      }
    }
    var fetcher;
    if (true) {
      var subscriptionsClient = new window.SubscriptionsTransportWs.SubscriptionClient('${subscriptionsEndpoint}', {
        reconnect: true
      });
      fetcher = window.GraphiQLSubscriptionsFetcher.graphQLFetcher(subscriptionsClient, graphQLFetcher);
    } else {
      fetcher = graphQLFetcher;
    }
    // We don't use safe-serialize for location, because it's not client input.
    var fetchURL = locationQuery(otherParams, '${endpointURL}');
    // Defines a GraphQL fetcher using the fetch API.
    function graphQLFetcher(graphQLParams) {
        return fetch(fetchURL, {
          method: 'post',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Sec-WebSocket-Protocol': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJpZCI6Ii1MRk5felRQN3hmak5YWmltd0hYIiwiZmlyc3RfbmFtZSI6Ilpha2FyaXlhIiwibGFzdF9uYW1lIjoiSHVzc2VpbiIsImZpcnN0TmFtZSI6Ilpha2FyaXlhIiwibGFzdE5hbWUiOiJIdXNzZWluIiwiZW1haWwiOiJ6YWthcml5YS5odXNzZWluQGFuZGVsYS5jb20iLCJuYW1lIjoiWmFrYXJpeWEgSHVzc2VpbiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vLTN3Qk96SXBOcVdvL0FBQUFBQUFBQUFJL0FBQUFBQUFBQUFBL0FHRGd3LWlpMkpLWWJNWFYxcTJCdTBQVjA0RFhTVlptTGcvbW8vcGhvdG8uanBnP3N6PTUwIiwicm9sZXMiOnsiRmVsbG93IjoiLUtYR3kxRUIxb2ltalFnRmltNkMiLCJBbmRlbGFuIjoiLUtpaWhmWm9zZVFlcUM2YldUYXUifX0sImlhdCI6MTU0MzQ4MjYxOSwiZXhwIjoxNTQ2MDc0NjE5LCJhdWQiOiJhbmRlbGEuY29tIiwiaXNzIjoiYWNjb3VudHMuYW5kZWxhLmNvbSJ9.cwHrftDNrNpcQhnSy6XPmdZmW6RhYdaZXWor70P8rfvecQ_fFnj8Y9h1-8n8G1HDhzzSVBNfsbjOxLKgRuTwxgpzLxLotpJV4KiCGLPtCFLkBUlWD8_y6maI5hJxjAyfsR6WZOx0VUE76ywRceWxtkzb9R4w4mYcvtaejxMP6I0'
          },
          body: JSON.stringify(graphQLParams),
          credentials: 'include',
        }).then(function (response) {
          return response.text();
        }).then(function (responseBody) {
          try {
            return JSON.parse(responseBody);
          } catch (error) {
            return responseBody;
          }
        });
    }
    // When the query and variables string is edited, update the URL bar so
    // that it can be easily shared.
    function onEditQuery(newQuery) {
      parameters.query = newQuery;
      updateURL();
    }
    function onEditVariables(newVariables) {
      parameters.variables = newVariables;
      updateURL();
    }
    function onEditOperationName(newOperationName) {
      parameters.operationName = newOperationName;
      updateURL();
    }
    function updateURL() {
      history.replaceState(null, null, locationQuery(parameters) + window.location.hash);
    }
    // Render <GraphiQL /> into the body.
    ReactDOM.render(
      React.createElement(GraphiQL, {
        fetcher: fetcher,
        onEditQuery: onEditQuery,
        onEditVariables: onEditVariables,
        onEditOperationName: onEditOperationName,
      }),
      document.body
    );
  </script>
</body>
</html>''').substitute(
        GRAPHIQL_VERSION='0.11.7',
        SUBSCRIPTIONS_TRANSPORT_VERSION='0.7.0',
        subscriptionsEndpoint='ws://localhost:5000/subscriptions',
        # subscriptionsEndpoint='ws://localhost:5000/',
        endpointURL='/mrm',
    )


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    FlaskJSON(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)
    socket.init_app(app)

    @app.route("/", methods=['GET'])
    def index():
        return render_template('index.html')

    subscription_server = GeventSubscriptionServer(schema)
    app.app_protocol = lambda environ_path_info: 'graphql-ws'

    @socket.route('/subscriptions')
    def echo_socket(ws):
        subscription_server.handle(ws)
        return []

    @app.route('/graphiql')
    def graphql_view():
        return make_response(render_graphiql())

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
