from sql_alchemy import database


class UserModel(database.Model):
    __tablename__ = 'sites'

    site_id = database.Column(database.Integer, primary_key=True)
    url = database.Column(database.String(80))

    def __init__(self: object, url: str) -> None:
        self.url = url

    def json(self) -> dict:
        return {
            'site_id': self.site_id,
            'url': self.url,
            'hotels': list()
        }

    @classmethod
    def find_site(cls: object, site_id: int) -> object or None:
        site = cls.query.filter_by(site_id=site_id).first()
        return site if site else None

    @classmethod
    def find_user_by_url(cls: object, url: str) -> object or None:
        site = cls.query.filter_by(url=url).first()
        return site if site else None

    def save_site(self: object) -> None:
        database.session.add(self)
        database.session.commit()

    def delete_site(self: object) -> None:
        database.session.delete(self)
        database.session.commit()



