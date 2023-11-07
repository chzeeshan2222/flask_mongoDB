from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token,JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
bcrypt=Bcrypt(app)
jwt=JWTManager(app)
from auth_app.db import config
from auth_app.routes import route

