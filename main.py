from flask import Blueprint


main = Blueprint('main', __name__, url_prefix="/api/v1/")


@main.route("/test")
def index():
    return 'Test is up'
