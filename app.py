from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Hoteis(Resource):
    def get(self):
        return {"Hoteis:": "Minha lista de hoteis"}


api.add_resource(Hoteis, '/hoteis')
print(__name__)

if __name__ == '__main__':
    app.run(debug=True)
