from extensions import api
from data.resources import Data
from users.resources import Users#, UserDetail, UserLogin
from services.resources import LeinData

# user routes
#api.add_resource(UserLogin, '/users/login')
api.add_resource(Users, '/users')
#api.add_resource(UserDetail, '/users/<string:user_id>')


# data routes
api.add_resource(Data, '/data')

# service routes
#api.add_resource(LeinData, '/lein-data')