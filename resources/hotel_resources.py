from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
import sqlite3

from models.site_model import SiteModel
from models.hotel_model import HotelModel
from utils.messages import *
from resources.filters_and_queries import with_city_query, without_city_query, normalize_path_params

# path params
path_params = reqparse.RequestParser()
path_params.add_argument('cidade', type=str, )
path_params.add_argument('estrelas_min', type=float)
path_params.add_argument('estrelas_max', type=float)
path_params.add_argument('diaria_max', type=float)
path_params.add_argument('diaria_min', type=float)
path_params.add_argument('limit', type=int)
path_params.add_argument('offset', type=int)

# body params
body = reqparse.RequestParser()
body.add_argument('nome', type=str, required=True, help=field_help)
body.add_argument('estrelas', type=str, required=False, help=field_help)
body.add_argument('diaria', type=float, required=False, help=field_help)
body.add_argument('cidade', type=str, required=False, help=field_help)
body.add_argument('site_id', type=int, required=True, help="Every hotel needs to be linked with a site.")


class Hotels(Resource):

    def get(self):
        connection = sqlite3.connect('flaskAPI.db')
        cursor = connection.cursor()

        data = path_params.parse_args()
        valid_data = {key: data[key] for key in data if data[key] is not None}
        params = normalize_path_params(**valid_data)

        if not params.get('cidade'):
            params_tuple = tuple([params[key] for key in params])
            res = cursor.execute(without_city_query, params_tuple)
        else:
            params_tuple = tuple([params[key] for key in params])
            res = cursor.execute(with_city_query, params_tuple)

        hotels = list()
        for row in res:
            hotels.append({
                'hotel_id': row[0],
                'nome': row[1],
                'estrelas': row[2],
                'diaria': row[3],
                'cidade': row[4],
                'site_id': row[5]
            })
        return hotels  # SELECT * FROM hoteis

    @jwt_required
    def post(self: object) -> object or dict:
        data = body.parse_args()
        hotel = HotelModel(**data)
        existing_hotel = HotelModel.find_hotel_by_name(data.nome)
        if not SiteModel.find_site(data['site_id']):
            return {'message': 'The hotel must be associated to a valid site id.'}
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
