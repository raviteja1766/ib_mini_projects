from abc import ABC
from abc import abstractmethod
from typing import List, Any
from common.dtos import UserAuthTokensDTO


class PresenterInterface(ABC):

    @abstractmethod
    def get_response_for_login_user(
            self, user_auth_token_dto: UserAuthTokensDTO):
        pass

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass