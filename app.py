from flask import Flask
from dbConfig import dbconnect
from database import db
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
import threading
import time
from flask_cors import CORS
app = Flask(__name__)
app.config.from_object(dbconnect.Config)
db.init_app(app)

from api.user_api_routes import user_route
app.register_blueprint(user_route)
CORS(app, origins='*')



