from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
import pytest
from content_management_portal.constants.exception_messages\
    import INVALID_ROUGH_SOLUTION_EXCEPTION
from django_swagger_utils.drf_server.exceptions import NotFound

def test_raise_exception_for_invalid_rough_solution_raises_exception():

    # Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_ROUGH_SOLUTION_EXCEPTION[0]

    # Act
    with pytest.raises(NotFound) as e:
        presenter.raise_exception_for_invalid_rough_solution()

    # Assert
    assert str(e.value) == exception_messages