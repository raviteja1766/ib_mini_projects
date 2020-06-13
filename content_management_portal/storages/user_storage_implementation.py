from content_management_portal.interactors.storages.user_storage_interface\
    import UserStorageInterface
from content_management_portal.models import User
from content_management_portal.exceptions.exceptions import InvalidPassword


class UserStorageImplementation(UserStorageInterface):

    def validate_username(self, username: str):

        return User.objects.filter(username=username).exists()

    def validate_password_to_user(self, username: str, password: str):

        user_obj = User.objects.get(username=username)
        is_invalid_password = not user_obj.check_password(password)
        if is_invalid_password:
            raise InvalidPassword
        return user_obj.id
