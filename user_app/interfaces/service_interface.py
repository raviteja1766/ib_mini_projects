from typing import List

from user_app.interactors.get_user_details_interactor import \
    GetUserDetailsInteractor
from user_app.storages.user_storage_implementation \
    import UserStorageImplementation


class ServiceInterface:

    @staticmethod
    def get_user_dtos(user_ids: List[int]):
        storage = UserStorageImplementation()
        interactor = GetUserDetailsInteractor(user_storage=storage)
        user_dtos = interactor.get_user_details_dtos(user_ids=user_ids)
        return user_dtos
