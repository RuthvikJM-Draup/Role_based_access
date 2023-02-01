from resources.user import UsersApi, UpdateUserApi, OneUserApi, DeleteUserApi, AddUserApi
from resources.auth import SignupApi, LoginApi


def initialize_routes(api):
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(AddUserApi, '/api/adduser')
    api.add_resource(UpdateUserApi, '/api/update/<_id>')
    api.add_resource(DeleteUserApi, '/api/delete/<_id>')
    api.add_resource(OneUserApi, "/api/user/<_id>")
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
