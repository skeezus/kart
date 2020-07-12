# -*- coding: utf-8 -*-
import os
from datetime import timedelta

# flask core settings
DEBUG = True
TESTING = False
ENVIRONMENT = os.getenv('ENVIRONMENT')
# random key generator: python -c 'import os; print(os.urandom(16))'
# secret key is what makes hash unique beyond user email
# if two companies use the same hash and email, the same token will be generated
SECRET_KEY = os.getenv('FLASK_SECRET')
PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 30

# flask wtf settings
WTF_CSRF_ENABLED = True

# database config
# database config
"""MONGODB_SETTINGS = {
    'db': os.getenv('DB_NAME'),
    'host': os.getenv('DB_IP'),
    'port': 27017,
    'authentication_source': 'admin',
    'username': 'root',
    'password': os.getenv('DB_PASS')
}"""

"""MONGODB_DB = os.getenv('DB_NAME')
MONGODB_HOST = os.getenv('DB_IP')
MONGODB_PORT = 27017
MONGODB_USERNAME = 'root'
MONGODB_PASSWORD = os.getenv('DB_PASS')
MONGODB_AUTHENTICATION_SOURCE = 'admin'"""

# jwt config
JWT_SECRET_KEY = os.getenv('JWT_SECRET')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=10000000)

MAPBOX_ACCESS_KEY = os.getenv('MAPBOX_ACCESS_KEY')

# API Keys
#SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
#SPOTIFY_SECRET = os.getenv('SPOTIFY_SECRET')

# project settings
#PROJECT_PASSWORD_HASH_METHOD = 'pbkdf2:sha1'
#PROJECT_SITE_NAME = u'Flask Example'
#PROJECT_SITE_URL = 'http://0.0.0.0:5000'
#PROJECT_SIGNUP_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds
#PROJECT_RECOVER_PASSWORD_TOKEN_MAX_AGE = 60 * 60 * 24 * 7  # in seconds

#turn off flask's sqlalchemy modification tracker
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'tuhg4512'
#app.config['MYSQL_DB'] = 'video_project_db'
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:tuhg4512@127.0.0.1:3306/video_project_db'
#app.config.update(
    #TESTING=True,
    #SECRET_KEY='_5#y2L"F4Q8z\n\xec]/'
#)
#app.secret_key = 'secret_key_12345'
