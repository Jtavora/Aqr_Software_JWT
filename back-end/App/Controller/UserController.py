from App.Models import UserModel
from App.Models import PermissionModel
from App.Auth import crypto

class UserController:
    def __init__(self):
        self.all_permissions = [permission['name'] for permission in PermissionModel.get_all_permissions()]

    def create_user(self, user_data):
        hashed_password = crypto.hash(user_data.hashed_password)
        new_user = UserModel(
            username=user_data.username,
            hashed_password=hashed_password,
            role=user_data.role
        )

        if new_user.role not in self.all_permissions:
            return None

        user_id = UserModel.create_user(new_user)
        return user_id

    def get_user_by_username(self, username):
        user = UserModel.get_user_by_username(username)
        if user:
            return user
        return None

    def get_all_users(self):
        users = UserModel.get_all_users()
        return [user for user in users]