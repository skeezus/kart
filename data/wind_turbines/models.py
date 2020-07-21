import datetime
from bson.json_util import dumps

from extensions import db


# http://docs.mongoengine.org/apireference.html
class WindTurbine(db.Document):
    _id = db.ObjectIdField()
    case_id = db.IntField(unique=True) # Unique stable identification number.
    faa_ors = db.StringField() # Unique identifier for cross-reference to the Federal Aviation Administration (FAA) digital obstacle files.
    faa_asn = db.StringField() # Unique identifier for cross-reference to the FAA obstruction evaluation airport airspace analysis dataset.
    usgs_pr_id = db.IntField() # Unique identifier for cross-reference to the 2014 USGS turbine dataset.
    t_state = db.StringField() # State where turbine is located.
    t_county = db.StringField() # County where turbine is located.
    t_fips = db.StringField() # State and county fips where turbine is located, based on spatial join of turbine points with US state and county.
    p_name = db.StringField() # Name of the wind power project that the turbine is a part of
    p_year = db.IntField() # Year that the turbine became operational and began providing power. Note this may differ from the year that construction began.
    p_tnum = db.IntField() # Number of turbines in the wind power project.
    p_cap = db.FloatField() # Cumulative capacity of all turbines in the wind power project in megawatts (MW).
    t_manu = db.StringField() # Turbine manufacturer - name of the original equipment manufacturer of the turbine.
    t_model = db.StringField() # Turbine model - manufacturer's model name of each turbine.
    t_cap = db.IntField() # Turbine rated capacity - stated output power at rated wind speed from manufacturer, AWEA, and/or internet resources in kilowatts (kW).
    t_hh = db.FloatField() # Turbine hub height in meters (m).
    t_rd = db.FloatField() # Turbine rotor diameter in meters (m).
    t_rsa = db.FloatField() # Turbine rotor swept area in square meters (m2).
    t_ttlh = db.FloatField() # Turbine total height from ground to tip of a blade at its apex in meters (m).
    t_conf_atr = db.IntField() # Level of confidence in the turbine attributes (1 - no confidence, 3 - full confidence)
    t_conf_loc = db.IntField() # Level of confidence in turbine location (1 - no turbine in image, 3 - turbine in image)
    t_img_date = db.DateTimeField() # Date of image used to visually verify turbine location.
    t_img_srce = db.StringField() # Source of image used to visually verify turbine location.
    longitude = db.FloatField() # Longitude of the turbine point, in decimal degrees.
    latitude = db.FloatField() # Latitude of the turbine point, in decimal degrees.
    eia_id = db.IntField() # Plant ID from Energy Information Administration (EIA).
    #updated = db.DateTimeField()
    created = db.DateTimeField(default=datetime.datetime.utcnow)
    
    meta = {
        'collection': 'wind_turbines'
    }

    # https://stackoverflow.com/questions/10252010/serializing-class-instance-to-json
    # https://stackoverflow.com/questions/7907596/json-dumps-vs-flask-jsonify
    # https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable
    def to_json(self):
        return {'id': str(self._id), 'name': self.p_name, 'latitude': self.latitude, 'longitude': self.longitude}