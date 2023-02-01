from flask import Response, request
from database.models import Details, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, DetailsAlreadyExistsError, InternalServerError, \
     UpdatingDetailsError, DeletingDetailsError, DetailsNotExistsError


class UsersApi(Resource):
    @jwt_required()
    def get(self):
        identity = get_jwt_identity()
        admin = User.objects.get(id=identity)
        if admin["role"] == "admin":
            users = Details.objects().to_json()
            return Response(users, mimetype="application/json", status=200)
        else:
            return 'User not valid', 500

    @jwt_required()
    def post(self):
        try:
            identity = get_jwt_identity()
            admin = User.objects.get(id=identity, role='admin')
            body = request.get_json()
            get_details = Details(**body, added_by=admin)
            get_details.save()
            admin.save()
            _id = get_details.id
            return {'id': str(_id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise DetailsAlreadyExistsError
        except Exception:
            raise InternalServerError


class UpdateUserApi(Resource):
    @jwt_required()
    def put(self, _id):
        try:
            identity = get_jwt_identity()
            admin = User.objects.get(role="admin")
            if admin["role"] == "admin":
                body = request.get_json()
                Details.objects.get(id=_id, added_by=identity).update(**body)
                return 'Updated', 200
            else:
                return 'Not Updated', 500
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingDetailsError

    @jwt_required()
    def delete(self, _id):
        try:
            user_id = get_jwt_identity()
            admin = User.objects.get(role="admin")
            if admin["role"] == "admin":
                user = Details.objects.get(id=_id, added_by=user_id)
                user.delete()
                return 'deleted', 200
            else:
                return 'Only admin can delete', 500
        except DoesNotExist:
            raise DeletingDetailsError


class OneUserApi(Resource):
    @jwt_required()
    def get(self, _id):
        try:
            users = Details.objects.get(id=_id).to_json()
            return Response(users, mimetype="application/json", status=200)
        except DoesNotExist:
            raise DetailsNotExistsError
        except Exception:
            raise InternalServerError
