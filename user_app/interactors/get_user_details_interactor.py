
from typing import List

from user_app.interactors.storages.user_storage_interface\
    import UserStorageInterface
from user_app.exceptions.exceptions import DuplicateUserIds, InvalidUserIds


class GetUserDetailsInteractor:

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_user_details_wrapper(self, user_ids: List[int]):

        user_dtos = self.get_user_details_dtos(user_ids=user_ids)
        return user_dtos

    def get_user_details_dtos(self, user_ids: List[int]):

        self._validations_for_user_ids(user_ids=user_ids)

        user_dtos = self.user_storage.get_user_details_dtos(user_ids=user_ids)
        return user_dtos

    def _validations_for_user_ids(self, user_ids: List[int]):

        self._validation_for_duplicate_user_ids(user_ids)
        valid_user_ids = \
            self.user_storage.get_valid_user_ids(user_ids=user_ids)
        invalid_user_ids = [
            user_id for user_id in user_ids if user_id not in valid_user_ids
        ]
        is_invalid_users_present = invalid_user_ids
        if is_invalid_users_present:
            raise InvalidUserIds(user_ids=invalid_user_ids)

    def _validation_for_duplicate_user_ids(self, user_ids: List[int]):

        from collections import Counter

        duplicate_ids = [
            item for item, count in Counter(user_ids).items()
            if count > 1
        ]
        is_duplicate_ids_present = duplicate_ids
        if is_duplicate_ids_present:
            raise DuplicateUserIds(user_ids=duplicate_ids)
