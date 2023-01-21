from flask import Flask

from api import root_bp

app = Flask(__name__)


app.register_blueprint(root_bp)
