from com_cheese_api.home.api import Home
from com_cheese_api.cheese.api import Cheese
from com_cheese_api.recommend.api import Recommend
from com_cheese_api.signin.api import SignIn
from com_cheese_api.fnq.api import Fnq


def initialize_routes(api):
    api.add_resource(Home, '/api')
    api.add_resource(Cheese, '/cheese')
    api.add_resource(Recommend, '/recommend')
    api.add_resource(SignIn, '/signin')
    api.add_resource(Fnq, '/fnq')
