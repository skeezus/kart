# -*- coding: utf-8 -*-
from flask import Flask
from extensions import api, cors, db, jwt
#from users.models import User

# application factory, see: http://flask.pocoo.org/docs/patterns/appfactories/
def create_app():
    # name is a pre-defined python variable which is set to the name of the module in which it is used
    # the flask object implements a WSGI application - once it is created it acts as a central repository
    # for view functions, url rules, template config, etc
    # should be created in main module or __init__.py of your package
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'kart_db',
        'host': '172.21.0.2',
        'port': 27017,
        'authentication_source': 'admin',
        'username': 'root',
        'password': 'tuhg4512'
    }
    #print('cf: ' + str(dir(config_filename)))
    #app.config.from_object('settings')
    app.config.from_envvar('FLASK_MODULE_SETTINGS')
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:tuhg4512@127.0.0.1:3306/mange_takk_db'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize extensions so that extension knows the name of the application object
    api.init_app(app)
    cors.init_app(app)
    # right now all cross origin requests are allowed - need to change this config
    # src: https://stackoverflow.com/questions/26980713/solve-cross-origin-resource-sharing-with-flask
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)
    jwt.init_app(app)

    return app

from routes import *
