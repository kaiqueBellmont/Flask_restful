from flask_restful import Resource, reqparse
from models.hotels_model import HotelModel
from utils.messages import *
from flask_jwt_extended import jwt_required

body = reqparse.RequestParser()

body.add_argument('nome', type=str, required=True, help=field_help)
body.add_argument('estrelas', type=str, required=False, help=field_help)
body.add_argument('diaria', type=float, required=False, help=field_help)
body.add_argument('cidade', type=str, required=False, help=field_help)


class Hotels(Resource):

    def get(self):
        return [hotel.json() for hotel in HotelModel.query.all()]  # SELECT * FROM hoteis

    @jwt_required
    def post(self: object) -> object or dict:
        data = body.parse_args()
        hotel = HotelModel(**data)

        existing_hotel = HotelModel.find_hotel_by_name(data.nome)
        if existing_hotel:
            return {"message": "Hotel '{}' already exists".format(data.nome)}
        try:
            hotel.save_hotel()
        except:
            return not_found, 500
        finally:
            return hotel.json(), 201


class Hotel(Resource):

    def get(self: object, hotel_id: int) -> object or dict:
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return not_found, 404

    @jwt_required
    def put(self: object, hotel_id: int) -> object or dict:
        data = body.parse_args()
        hotel = HotelModel(**data)
        hotel_found = HotelModel.find_hotel(hotel_id)
        if hotel_found:
            hotel_found.update_hotel(**data)
            hotel_found.save_hotel()
            return hotel_found.json(), 200
        hotel.save_hotel()
        return hotel.json(), 201

    @jwt_required
    def delete(self: object, hotel_id: int) -> object or dict:
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'Hotel deleted.'}
        return not_found, 404
