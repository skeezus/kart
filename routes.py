from extensions import api
from data.resources import Data
from data.wind_turbines.resources import WindTurbines
from users.resources import Users#, UserDetail, UserLogin
from services.resources import LeinData

# user routes
#api.add_resource(UserLogin, '/users/login')
api.add_resource(Users, '/users')
#api.add_resource(UserDetail, '/users/<string:user_id>')


# data routes
api.add_resource(Data, '/data')
api.add_resource(WindTurbines, '/data/wind-turbines') # wind turbine routes

# service routes
#api.add_resource(LeinData, '/lein-data')