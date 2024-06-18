from flask import Blueprint, request
import services.user_services as user_services

user_route = Blueprint('user_route', __name__)
from utils.JwtToken import validate_token_admin


@user_route.route("/api/v1/user/register", methods=['POST'])
def register():
    data = request.get_json()
    return user_services.register(data)

@user_route.route("/api/v1/user/login", methods=['POST'])
def login():
    data = request.get_json()
    return user_services.login(data)


