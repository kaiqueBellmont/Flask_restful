from flask import Flask
from flask_restful import Api
from resources.hotel_resources import Hotels, Hotel
from resources.user_resources import User, UserRegister

app: Flask = Flask(__name__)

"""Create a name.db in the project root"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskAPI.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_database() -> None:
    database.create_all()


""" instantiates routes according to class """
api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotel/<int:hotel_id>')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from sql_alchemy import database

    database.init_app(app)
    app.run(debug=True, port=5000)
