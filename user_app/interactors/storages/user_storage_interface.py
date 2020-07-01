from abc import ABC
from abc import abstractmethod
from typing import Optional, List
from user_app.interactors.storages.dtos import UserDto


class UserStorageInterface(ABC):

    @abstractmethod
    def validate_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def validate_password_to_user(
            self, username: str, password: str) -> Optional[int]:
        pass

    @abstractmethod
    def get_valid_user_ids(self, user_ids: List[int]) -> Optional[List[int]]:
        pass

    @abstractmethod
    def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDto]:
        pass
