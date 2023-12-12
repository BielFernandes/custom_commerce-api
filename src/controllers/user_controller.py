from src.models.User import User, db
from src.models.Address import Address

class UserController:
    def index(self):
        squidward = User(name="squidward", fullname="Squidward Tentacles")
        krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")
        db.session.add(squidward)
        db.session.add(krabs)
        print(db.session.new)
        db.session.commit()
        return 'okok', 200
        