from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
import pytest
from content_management_portal.constants.exception_messages\
    import INVALID_SOLUTION_APPROACH_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound


def test_raise_exception_for_invalid_solution_approach():

    # Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_SOLUTION_APPROACH_EXCEPTION[0]

    # Act
    with pytest.raises(NotFound) as e:
        presenter.raise_exception_for_invalid_solution_approach()

    # Assert
    assert str(e.value) == exception_messages
