from resources.user import UsersApi, UserApi, OneUserApi
from resources.auth import SignupApi, LoginApi


def initialize_routes(api):
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/user/<_id>')
    api.add_resource(OneUserApi, '/api/oneUser/<_id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
