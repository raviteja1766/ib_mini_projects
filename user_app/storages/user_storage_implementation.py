from typing import Optional, List
from user_app.interactors.storages.user_storage_interface\
    import UserStorageInterface
from user_app.models import User
from user_app.interactors.storages.dtos import UserDto
from user_app.exceptions.exceptions import InvalidPassword, InvalidUsername


class UserStorageImplementation(UserStorageInterface):

    def validate_username(self, username: str):

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUsername

    def validate_password_to_user(self, username: str, password: str):

        user_obj = User.objects.get(username=username)
        is_invalid_password = not user_obj.check_password(password)
        if is_invalid_password:
            raise InvalidPassword
        return user_obj.id


    def get_valid_user_ids(self, user_ids: List[int]) -> Optional[List[int]]:

        return list(
            User.objects.filter(id__in=user_ids).values_list('id', flat=True)
        )


    def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDto]:

        user_objs = list(User.objects.filter(id__in=user_ids))
        return [
            self._convert_user_obj_to_dto(user_obj)
            for user_obj in user_objs
        ]

    def _convert_user_obj_to_dto(self, user_obj):

        return UserDto(
            user_id=user_obj.id,
            username=user_obj.username
        )
