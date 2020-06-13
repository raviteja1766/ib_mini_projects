from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
import pytest
from content_management_portal.constants.exception_messages\
    import INVALID_QUESTION_EXCEPTION
from django_swagger_utils.drf_server.exceptions import Forbidden


def test_raise_exception_for_different_question_raises_exception():

    # Arrange
    presenter = PresenterImplementation()
    exception_messages = INVALID_QUESTION_EXCEPTION[0]

    # Act
    with pytest.raises(Forbidden) as e:
        presenter.raise_exception_for_different_question()

    # Assert
    assert str(e.value) == exception_messages
