from flask import Flask, jsonify
from flask_restful import Api
from resources.hotel_resources import Hotels, Hotel
from resources.user_resources import User, UserRegister, UserConfirm, UserLogin, UserLogout
from resources.site_resourses import Sites, Site
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST


app: Flask = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskAPI.db'  # Create a name.db in the project root
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def create_database() -> None:
    database.create_all()


@jwt.token_in_blacklist_loader
def token_verify(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def invalid_access_token():
    return jsonify({'message': 'Token has been revoked'}), 401


""" instantiates routes according to class """
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserConfirm, '/confirmation/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotel/<int:hotel_id>')

api.add_resource(Sites, '/sites')
api.add_resource(Site, '/site/<string:url>')

if __name__ == '__main__':
    from sql_alchemy import database

    database.init_app(app)
    app.run(debug=True, port=5000)
