from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
import pytest
from content_management_portal.constants.exception_messages\
    import INVALID_PASSWORD_EXCEPTION
from django_swagger_utils.drf_server.exceptions import Unauthorized


def test_raise_exception_for_invalid_username_raises_exception():

    # Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_PASSWORD_EXCEPTION[0]

    # Act
    with pytest.raises(Unauthorized) as e:
        presenter.raise_exception_for_invalid_password()

    # Assert
    assert str(e.value) == exception_messages
