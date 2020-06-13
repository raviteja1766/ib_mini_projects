from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
import pytest
from content_management_portal.constants.exception_messages\
    import SOLUTION_APPROACH_ALREADY_EXISTS
from django_swagger_utils.drf_server.exceptions import BadRequest


def test_raise_exception_for_invalid_solution_approach():

    # Arrange
    presenter = PresenterImplementation()
    exception_messages = SOLUTION_APPROACH_ALREADY_EXISTS[0]

    # Act
    with pytest.raises(BadRequest) as e:
        presenter.raise_exception_for_solution_approach_exists()

    # Assert
    assert str(e.value) == exception_messages
