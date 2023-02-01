from flask import request
from flask_jwt_extended import create_access_token
from database.models import User
from flask_restful import Resource
import datetime


class SignupApi(Resource):
    @staticmethod
    def post():
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        _id = user.id
        return {'id': str(_id)}, 200


class LoginApi(Resource):
    @staticmethod
    def post():
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
