from flask import request, jsonify
from sqlalchemy import select
from marshmallow import ValidationError
from sqlalchemy.ext.serializer import loads, dumps
from src.schemas.user import UserSchema
from src.models.User import User, db
from datetime import date

class UserController:
    def index(self):
        # squidward = User(
        #                     fname="Gabriel",
        #                     lname="Fernandes",
        #                     email="asdasdasda@gmail.com",
        #                     password="bieldias882",
        #                     admin=True,
        #                 )
        # db.session.add(squidward)
        # print(db.session.new)
        # db.session.commit()
        return 'okok', 200
        
    def create(self):
        today = date.today()
        data = request.get_json()
        data['admin'] = False
        data['created_at'] = today.isoformat()

        if not data: return { "message": "No input data provided" }, 400

        if data['password'] != data['confirm_password']: return { "message": "senhas divergem" }, 400

        data.pop("confirm_password")

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
        