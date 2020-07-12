import csv
import io

from flask import request
from flask_restful import Resource, reqparse


data_parser = reqparse.RequestParser(bundle_errors=True)
data_parser.add_argument('csv_file', required=True, location='files', help='Make sure to include a file.')

class Data(Resource):

    def post(self):
        data_parser.parse_args()
        file_obj = request.files['csv_file']

        if file_obj.content_type == 'text/csv':
            # csv_file.filename # name of file
            file = file_obj.read().decode('utf-8-sig').splitlines()
            reader = csv.DictReader(file) # don't need with/open bc file is in memory already

            json = []

            for row in reader:
                json.append(row)
        else:
            return 'Make sure to include a CSV file with your request', 400

        return json