from flask_restful import Resource

import utils.messages
from models.site_model import SiteModel
from utils.messages import *


class Sites(Resource):
    def get(self: object) -> list:
        return list(site.json() for site in SiteModel.query.all())


class Site(Resource):
    def get(self: object, url: str) -> object:
        site = SiteModel.find_user_by_url(url)
        return site.json() if site else not_found, 404

    def post(self: object, url: str) -> object:
        if SiteModel.find_user_by_url(url):
            return {"message": "the site '{}' already exists."}, 400
        site = SiteModel(url)
        try:
            site.save_site()
        except:
            return {'message': 'An internal error ocurred trying to create a new site.'}
        return site.json()

    def delete(self: object, url: str) -> object:
        site = SiteModel.find_user_by_url(url=url)
        if site:
            site.delete_site()
            return {'message': 'Site deleted.'}
        return {'message': 'Site not found'}, 404
