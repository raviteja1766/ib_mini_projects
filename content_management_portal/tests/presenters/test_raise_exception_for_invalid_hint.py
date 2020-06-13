import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.constants.exception_messages\
    import INVALID_HINT_EXCEPTION

def test_raise_exception_for_invalid_hint_raises_exception():

    # Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_HINT_EXCEPTION[0]

    # Act
    with pytest.raises(NotFound) as e:
        presenter.raise_exception_for_invalid_hint()

    # Assert
    assert str(e.value) == exception_messages
