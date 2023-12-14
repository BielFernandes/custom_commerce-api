from flask import request
from sqlalchemy import select
from marshmallow import ValidationError
from src.schemas.user import UserSchema
from src.models.User import User, db
from datetime import date

class UserController:
    def index(self):
        squidward = User(
                            fname="Gabriel",
                            lname="Fernandes",
                            email="asdasdasda@gmail.com",
                            password="bieldias882",
                            admin=True,
                            created_at=today
                        )
        db.session.add(squidward)
        print(db.session.new)
        db.session.commit()
        return 'okok', 200
        
    def create(self):
        today = date.today()
        data = request.get_json()
        data['admin'] = False
        data['created_at'] = today.isoformat()

        if not data:
            return { "message": "No input data provided" }, 400

        try:
            user = UserSchema()
            data['password'] = user.hash_password(data['password'])
            data = user.load(data)
        except ValidationError as error:
            return error.messages, 422

        find_user = db.session.execute(select(User).where(User.email == data['email'])).all()

        if not find_user:
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            db.session.close()
            return { "message": "usuario criado" }, 201
        else:
            return { "message": "user already exist" }, 409
        