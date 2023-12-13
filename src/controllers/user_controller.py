from src.models.User import User, db
from src.models.Address import Address
from datetime import date
today = date.today()

class UserController:
    def index(self):
        squidward = User(
                            fname="Gabriel",
                            lname="Fernandes",
                            email="gabrieldias082@gmail.com",
                            password="bieldias882",
                            admin=True,
                            created_at=today
                        )
        db.session.add(squidward)
        print(db.session.new)
        db.session.commit()
        return 'okok', 200
        