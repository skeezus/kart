from flask import jsonify
from flask_restful import Resource

import json
from urllib import request as urllib_request, parse

class Geocode(object):

    #ACCESS_TOKEN = current_app.config['MAPBOX_ACCESS_KEY']
    QUERY_URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{0}.json?access_token={1}&limit=1&fuzzyMatch=false&country=US'

    def __init__(self, address, zip_code):
        self.address = address
        self.zip_code = zip_code

    # batch geocoding is only available with an enterprise mapbox plan
    def get_coordinates(self):
        query = self.build_query()
        resp = urllib_request.urlopen(query)
        data = json.load(resp)
        print(data)
        return data['features'][0]['geometry']['coordinates']
        #print(f.read())

    def build_query(self):
        # use urlencode because mapbox doesn't accept json, it accepts a url encoded query
        # https://stackoverflow.com/questions/9870523/differences-in-application-json-and-application-x-www-form-urlencoded
        # https://www.mapbox.com/help/troubleshooting/address-geocoding-format-guide/
        data = parse.urlencode({'address': self.address, 'postcode': self.zip_code, 'region': 'NY', 'place': 'New York'})

        return self.QUERY_URL.format(data, self.ACCESS_TOKEN)

    #def get

class LeinData(Resource):

    QUERY_URL = 'https://data.cityofnewyork.us/api/views/9rz4-mjek/rows.json'
    COLUMN_NAMES = ['position', 'id', 'position', 'created_at', 'created_meta', 'updated_at', 'updated_meta', 'meta', 
        'month', 'burough', 'block', 'lot', 'tax_class_code', 'building_class', 'community_board', 
        'council_district', 'house_number', 'street_name', 'zip_code', 'water_debt_only']

    def get(self):
        r = urllib_request.urlopen(self.QUERY_URL)
        #print(f.read())
        resp = json.load(r)
        data = resp['data']
        #print('length: ' + str(len(data)))
        
        # data type is list 
        page = data[0:20]
        page_with_columns = []
        for p in page:
            d = {key: value for (key, value) in zip(self.COLUMN_NAMES, p)}
            page_with_columns.append(d)

        for p in page_with_columns:
            address = '{0} {1}'.format(p['house_number'], p['street_name'])
            zip_code = p['zip_code']

            gc = Geocode(address, zip_code)
            coordinates = gc.get_coordinates()

            p['location'] = coordinates

        print(page_with_columns)
        return page_with_columns, 200
