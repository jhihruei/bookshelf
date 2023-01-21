from flask import Blueprint

root_bp = Blueprint("root_bp", __name__)


@root_bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
