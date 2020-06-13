import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.constants.exception_messages\
    import INVALID_OFFSET_LENGTH

def test_raise_exception_for_invalid_test_case_raises_exception():

    # Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_OFFSET_LENGTH[0]

    # Act
    with pytest.raises(BadRequest) as e:
        presenter.raise_exception_for_offset_exception()

    # Assert
    assert str(e.value) == exception_messages
