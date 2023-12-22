from flask import Blueprint
from src.controllers.user_controller import UserController
from src.middlewares.auth import token_required

user_blueprint = Blueprint('user_blueprint', __name__)

user_controller = UserController()

@user_blueprint.route('/', methods=['POST'])
def create_user():
    return user_controller.create()

@user_blueprint.route('/sign_in', methods=['POST'])
def login():
    return user_controller.login()

@user_blueprint.route('/me', methods=['DELETE'])
@token_required
def delete_user(current_user):
    return user_controller.delete(current_user)