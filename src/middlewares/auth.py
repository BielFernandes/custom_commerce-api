import jwt
from functools import wraps
from flask import request
from src.models.User import User, db
from src.schemas.user import UserSchema

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
          token = request.headers["Authorization"].split(" ")[1]
        if not token:
          return {
            "message": "Authentication Token is missing!",
            "data": None,
            "error": "Unauthorized"
          }, 401
        try:
          data=jwt.decode(token, "secret", algorithms=["HS256"])
          print('datazinhaaaaa',data)
          current_user=db.session.query(User).filter_by(email=data['email']).first()
          print('current_user',current_user)
          if current_user is None:
            return {
              "message": "Invalid Authentication token!",
              "data": None,
              "error": "Unauthorized"
            }, 401
        except Exception as e:
          print('erroooooooooo',e)
          return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
          }, 500

        # if find_user:
        user_schema = UserSchema()
        current_user = user_schema.dump(current_user)

        print('aaaaaaaaaaaaaaaaaa', current_user)

        return f(current_user, *args, **kwargs)
        
    return decorated