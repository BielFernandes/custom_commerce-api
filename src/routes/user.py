from flask import Blueprint
from src.controllers.user_controller import UserController

user_blueprint = Blueprint('user_blueprint', __name__)

user_controller = UserController()

user_blueprint.add_url_rule('/user', view_func=user_controller.index, methods=['GET'])

user_blueprint.add_url_rule('/user', view_func=user_controller.create, methods=['POST'])

user_blueprint.add_url_rule('/user/login', view_func=user_controller.login, methods=['POST'])

