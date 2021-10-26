from hmac import compare_digest

from flask_restful import Resource, reqparse
from models.user_model import UserModel
from utils.messages import *
from blacklist import BLACKLIST

from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt

body = reqparse.RequestParser()
body.add_argument('login', type=str, required=True, help=field_help)
body.add_argument('password', type=str, required=False, help=field_help)


class User(Resource):

    def get(self: object, user_id: int) -> object or dict:
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return not_found, 404

    @jwt_required
    def delete(self: object, user_id: int) -> object or dict:
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'User deleted.'}
        return not_found, 404


class UserRegister(Resource):
    def post(self):
        data = body.parse_args()
        if UserModel.find_user_by_login(data.login):
            return {"message:": "The login '{}' already exists!".format(data.login)}

        user = UserModel(**data)
        user.save_user()
        return {"message:": "user created sucessfully!"}, 201


class UserLogin(Resource):

    @classmethod
    def post(cls):
        data = body.parse_args()
        user = UserModel.find_user_by_login(data.login)

        if user and compare_digest(user.password, data.password):
            acess_token = create_access_token(identity=user.user_id)
            return {'access token': acess_token}, 200
        return {'message:': 'The username or password is incorrect.'}, 401


class UserLogout(Resource):
    @jwt_required
    def post(self):
        # JWT Token Identify
        jwt_id = get_raw_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully'}
