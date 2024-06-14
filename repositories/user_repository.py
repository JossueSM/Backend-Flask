from models.user import User, Profile
from app import db

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_user(username, profile_id):
    new_user = User(username=username, profile_id=profile_id)
    db.session.add(new_user)
    db.session.commit()
    return new_user
