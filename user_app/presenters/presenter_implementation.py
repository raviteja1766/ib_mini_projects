from django_swagger_utils.drf_server.exceptions import Unauthorized
from abc import ABC
from abc import abstractmethod
from typing import List, Any
from common.dtos import UserAuthTokensDTO
from user_app.interactors.presenters.presenter_interface\
    import PresenterInterface
from user_app.constants.exception_messages import *


class PresenterImplementation(PresenterInterface):

    def get_response_for_login_user(
            self, user_auth_token_dto: UserAuthTokensDTO):

        return {
            "user_id": user_auth_token_dto.user_id,
            "access_token": user_auth_token_dto.access_token,
            "refresh_token": user_auth_token_dto.refresh_token,
            "expires_in": str(user_auth_token_dto.expires_in)
        }


    def raise_exception_for_invalid_username(self):

        raise Unauthorized(*INVALID_USERNAME_EXCEPTION)

    def raise_exception_for_invalid_password(self):

        raise Unauthorized(*INVALID_PASSWORD_EXCEPTION)
