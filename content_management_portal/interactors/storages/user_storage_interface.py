from abc import ABC
from abc import abstractmethod
from typing import Optional


class UserStorageInterface(ABC):


    @abstractmethod
    def validate_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def validate_password_to_user(
            self, username: str, password: str) -> Optional[int]:
        pass
