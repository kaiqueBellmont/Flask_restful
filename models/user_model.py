from sql_alchemy import database


class UserModel(database.Model):
    __tablename__ = 'users'

    user_id = database.Column(database.Integer, primary_key=True)
    login = database.Column(database.String(40))
    password = database.Column(database.String(40))
    activated = database.Column(database.Boolean, default=False)

    def __init__(self: object, login: str, password: str, activated: bool) -> None:
        self.login = login
        self.password = password
        self.activated = activated

    def json(self) -> dict:
        return {
            'user_id': self.user_id,
            'login': self.login,
            'activated': self.activated
        }

    @classmethod
    def find_user(cls: object, user_id: int) -> object or None:
        user = cls.query.filter_by(user_id=user_id).first()
        return user if user else None

    @classmethod
    def find_user_by_login(cls: object, login: str) -> object or None:
        user = cls.query.filter_by(login=login).first()
        return user if user else None

    def save_user(self: object) -> None:
        database.session.add(self)
        database.session.commit()

    def delete_user(self: object) -> None:
        database.session.delete(self)
        database.session.commit()



