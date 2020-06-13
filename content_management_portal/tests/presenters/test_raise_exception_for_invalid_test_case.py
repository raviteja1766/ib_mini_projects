import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.constants.exception_messages\
    import INVALID_TESTCASE_EXCEPTION

def test_raise_exception_for_invalid_test_case_raises_exception():

    # Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_TESTCASE_EXCEPTION[0]

    # Act
    with pytest.raises(NotFound) as e:
        presenter.raise_exception_for_invalid_test_case()

    # Assert
    assert str(e.value) == exception_messages
