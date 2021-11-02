from sql_alchemy import database


class HotelModel(database.Model):
    __tablename__ = 'hotels'

    hotel_id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(80))
    estrelas = database.Column(database.Float(precision=1))
    diaria = database.Column(database.Float(precision=2))
    cidade = database.Column(database.String(40))
    site_id = database.Column(database.Integer, database.ForeignKey('sites.site_id'))

    def __init__(self: object, nome: str, estrelas: float, diaria: float, cidade: str, site_id: int) -> None:
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        self.site_id = site_id

    def json(self) -> object:
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade,
            'site_id': self.site_id
        }

    @classmethod
    def find_hotel(cls: object, hotel_id: int) -> object or None:
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        return hotel if hotel else None

    @classmethod
    def find_hotel_by_name(cls: object, hotel_name: str) -> object or None:
        hotel = cls.query.filter_by(nome=hotel_name).first()
        return hotel if hotel else None

    def save_hotel(self: object) -> None:
        database.session.add(self)
        database.session.commit()

    def update_hotel(self: object, nome: str, estrelas: float, diaria: float, cidade: str, site_id: int) -> None:
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        self.site_id = site_id

    def delete_hotel(self: object) -> None:
        database.session.delete(self)
        database.session.commit()
