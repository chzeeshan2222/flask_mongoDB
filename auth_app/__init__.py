from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
bcrypt=Bcrypt(app)

from .db.config import connect_to_db
# Connect to MongoDB
connect_to_db()
from auth_app.db import config
from auth_app.routes import route

