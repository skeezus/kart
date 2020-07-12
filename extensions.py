from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

api = Api()
bcrypt = Bcrypt()
cors = CORS()
jwt = JWTManager()
db = MongoEngine()
