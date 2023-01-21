from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api import root_bp

db = SQLAlchemy()
app = Flask(__name__)

app.register_blueprint(root_bp)
