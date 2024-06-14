from repositories.user_repository import get_all_users, create_user

def list_users():
    return get_all_users()

def add_new_user(username, profile_id):
    return create_user(username, profile_id)
