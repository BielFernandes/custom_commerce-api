from flask import request, make_response, jsonify, current_app, g
from sqlalchemy import select
from marshmallow import ValidationError
from src.schemas.user import UserSchema, LoginSchema, DeserializedUserSchema
from src.models.User import User, db
from datetime import date
# from src.controllers.application_controller import ApplicationController
import bcrypt
import jwt

class UserController():
      
  def create(self):
    today = date.today()
    data = request.get_json()
    data['admin'] = False
    data['created_at'] = today.isoformat()

    if not data: return { "message": "No input data provided" }, 400

    if data['password'] != data['confirm_password']: return { "message": "senhas divergem" }, 400

    data.pop("confirm_password")

    try:
      user = DeserializedUserSchema()
      data['password'] = user.hash_password(data['password'])
      data = user.load(data)
    except ValidationError as error:
      return error.messages, 422

    find_user = db.session.query(User).filter_by(email=data['email']).first()

    if not find_user:
      user = User(**data)
      db.session.add(user)
      db.session.commit()
      db.session.close()
      return { "message": "created user" }, 201
    else:
      return { "message": "user already exist" }, 409

  def login(self):
    data = request.get_json()
    
    if not data: return { "message": "No input data provided" }, 400

    try:
        login_schema = LoginSchema()
        data = login_schema.load(data)
    except ValidationError as error:
        return error.messages, 422

    find_user = db.session.query(User).filter_by(email=data['email']).first()

    if find_user:
      user_schema = UserSchema()
      user = user_schema.dump(find_user)
    
      user_pwd = data['password'].encode('utf-8')
      user_hash = user['password'].encode('utf-8')

      if bcrypt.checkpw(user_pwd, user_hash):
        encoded_jwt = jwt.encode(user, "secret", algorithm="HS256")
        
        response_data = {'message': 'Login successfully.'}
        my_response = make_response(response_data)
        my_response.headers['Authorization'] = f'Bearer {encoded_jwt}'
        my_response.content_type = "application/json"
        my_response.status_code = 201

        return my_response
      else:
        return { "message": "Incorrect email or password." }, 401
    else:
      return { "message": "Incorrect email or password." }, 401
      
  def delete(self, current_user):
    data = request.get_json()
    
    if not data: return { "message": "No input data provided" }, 400
    
    find_user = db.session.query(User).filter_by(id=current_user['id']).first()
    
    dbRegisterDeserializedUser = DeserializedUserSchema()
    registerForCompareWithRequest = dbRegisterDeserializedUser.dump(find_user)
    
    if find_user:
      user_pwd = data['password'].encode('utf-8')
      user_hash = registerForCompareWithRequest['password'].encode('utf-8')
      if not bcrypt.checkpw(user_pwd, user_hash):
        return { "message": "Incorrect user password." }
      else:
        user = db.session.get(User, current_user['id'])
        db.session.delete(user)
        db.session.commit()
        db.session.close()
        return { "message": "Deleted user" }
    else:
      return {"message": "User not found"}