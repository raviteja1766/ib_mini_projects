import pytest
import datetime
from unittest.mock import patch
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import Unauthorized
from user_app.exceptions.exceptions import InvalidPassword, InvalidUsername
from user_app.interactors.presenters.presenter_interface\
    import PresenterInterface
from user_app.interactors.storages.user_storage_interface\
    import UserStorageInterface
from common.oauth2_storage import OAuth2SQLStorage
from user_app.interactors.login_user_interactor\
    import LoginUserInteractor
from user_app.exceptions.exceptions import InvalidPassword
from common.oauth_user_auth_tokens_service\
    import OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO


def test_login_user_given_invalid_user_raises_exception_for_invalid_user():

    # Arrange
    username = "raviteja"
    password = "Maths@143"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()
    interactor = LoginUserInteractor(
        user_storage=user_storage, oauth_storage=oauth_storage,
        presenter=presenter
    )
    user_storage.validate_username.side_effect = InvalidUsername
    presenter.raise_exception_for_invalid_username.side_effect = Unauthorized

    # Act
    with pytest.raises(Unauthorized):
        interactor.login_user(username=username, password=password)

    # Assert
    user_storage.validate_username.assert_called_once_with(username=username)
    presenter.raise_exception_for_invalid_username.assert_called_once()


def test_login_user_given_invalid_password_raises_exception_for_invalid_password():

    # Arrange
    username = "raviteja"
    password = "Maths@143"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()
    interactor = LoginUserInteractor(
        user_storage=user_storage, oauth_storage=oauth_storage,
        presenter=presenter
    )
    user_storage.validate_username.return_value = None
    user_storage.validate_password_to_user.side_effect = InvalidPassword
    presenter.raise_exception_for_invalid_password.side_effect = Unauthorized

    # Act
    with pytest.raises(Unauthorized):
        interactor.login_user(username=username, password=password)

    # Assert
    user_storage.validate_username.assert_called_once_with(username=username)
    user_storage.validate_password_to_user.assert_called_once_with(
        username=username, password=password
    )
    presenter.raise_exception_for_invalid_password.assert_called_once()


@patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens')
def test_login_user_given_valid_details_returns_accesstoken_dto(
        user_auth_token):

    # Arrange
    userauthtoken = UserAuthTokensDTO(
        user_id=1, access_token="1OfS6IZWCum8Jgpudp6FcAnqfKAb7t",
        refresh_token="SLnTl4l4z07mW7s96AlBcuXBhvVeid",
        expires_in=datetime.datetime(5189, 4, 11, 9, 51, 25, 278085)
    )
    user_auth_token.return_value = userauthtoken
    presenter_response = {
        "access_token": "1OfS6IZWCum8Jgpudp6FcAnqfKAb7t",
        "refresh_token": "SLnTl4l4z07mW7s96AlBcuXBhvVeid",
        "expires_in": datetime.datetime(5189, 4, 11, 9, 51, 25, 278085)
    }
    user_id = 1
    username = "raviteja"
    password = "Maths@143"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = OAuth2SQLStorage()
    interactor = LoginUserInteractor(
        user_storage=user_storage, oauth_storage=oauth_storage,
        presenter=presenter
    )
    user_storage.validate_username.return_value = None
    user_storage.validate_password_to_user.return_value = user_id
    presenter.get_response_for_login_user.return_value = presenter_response

    # Act
    interactor_response = interactor.login_user(
        username=username, password=password)

    # Assert
    user_storage.validate_username.assert_called_once_with(username=username)
    user_storage.validate_password_to_user.assert_called_once_with(
        username=username, password=password
    )
    presenter.get_response_for_login_user\
        .assert_called_once_with(user_auth_token_dto=userauthtoken)
    assert interactor_response == presenter_response
