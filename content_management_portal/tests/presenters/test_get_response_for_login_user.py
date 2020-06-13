from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
import datetime
from common.dtos import UserAuthTokensDTO


def test_get_response_for_login_user_returns_access_token(
        user_auth_token_dto):

    # Arrange
    presenter = PresenterImplementation()
    expected_response = {
        "access_token": "1OfS6IZWCum8Jgpudp6FcAnqfKAb7t",
        "refresh_token": "SLnTl4l4z07mW7s96AlBcuXBhvVeid",
        "expires_in": str(datetime.datetime(5189, 4, 11, 9, 51, 25, 278085)),
        "user_id": 1
    }

    # Act
    actual_response = presenter.get_response_for_login_user(
        user_auth_token_dto=user_auth_token_dto)

    # Assert
    assert actual_response == expected_response
