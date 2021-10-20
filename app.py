from flask import Flask
from flask_restful import Api
from resources.hotel_resources import Hotels, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def cria_banco():
    database.create_all()


api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotel/<string:hotel_id>')

if __name__ == '__main__':
    from sql_alchemy import database

    database.init_app(app)
    app.run(debug=True, port=5000)
