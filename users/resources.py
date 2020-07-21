import json
import logging
from bson.json_util import dumps

from flask import request, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from .models import User


register_parser = reqparse.RequestParser(bundle_errors=True)
register_parser.add_argument('name', required=True, help='Make sure to include your first name.')
register_parser.add_argument('email', required=True, help='Make sure to include an email.')
register_parser.add_argument('password', required=True, help='Make sure to include a password.')

class Users(Resource):

    def post(self):
        args = register_parser.parse_args()
        if not request.content_type == 'application/json':
            return 'Content-type must be application/json', 400

        data = request.get_json()

        user = User.objects(email=data['email']) \
            .only('_id', 'name', 'email', 'password') \
            .first()
        if user is not None:
             return {'message': 'An account with that email already exists. Please try another.'}, 422
        # there's duplicate records in the database so we need to check manually
        user = User(**data)
        user.encrypt_password(data['password'])

        user.save()
        user = User.objects(email=data['email']) \
            .only('_id', 'name', 'email') \
            .first()

        # use the below if you want to return the actual object id
        #return json.loads(dumps(user)), 201 # Unlike Flask's jsonify, "dumps" will return a string, so it cannot be used as a 1:1 replacement of Flask's jsonify: https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable
        return user.to_json()

    def get(self):
        users = User.objects[:]
        #logging.debug(type(user))
        logging.warning(type(users))
        return jsonify(users)
        
