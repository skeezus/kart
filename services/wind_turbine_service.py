import json
import requests
from utils.url_builder import URLBuilder

BASE_URL = 'https://eersc.usgs.gov/api/uswtdb/v1/turbines'


def get_wind_turbines():

    builder = URLBuilder(BASE_URL)
    #builder.add_param('limit', '2')

    url = builder.build_url()

    resp = requests.get(url)
    return json.loads(resp.text)