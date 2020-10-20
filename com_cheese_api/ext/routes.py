from com_cheese_api.home.api import Home
def initialize_route(api):
    api.add_resource(Home, '/api')