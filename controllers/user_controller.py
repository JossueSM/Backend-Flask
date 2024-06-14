from flask import Blueprint, request, jsonify
from services.user_service import list_users, add_new_user

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = list_users()
    return jsonify([user.to_dict() for user in users])

@user_blueprint.route('/users', methods=['POST'])
def post_user():
    data = request.get_json()
    user = add_new_user(data['username'], data['profile_id'])
    return jsonify(user.to_dict()), 201
