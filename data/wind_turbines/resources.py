from bson import json_util
import json
import logging
from flask import request, jsonify
from flask_restful import Resource

from .models import WindTurbine
from services import wind_turbine_service


class WindTurbines(Resource):

    def get(self):
        turbines = WindTurbine.objects[:100]
        #logging.debug(turbines)
        return jsonify([t.to_json() for t in turbines])