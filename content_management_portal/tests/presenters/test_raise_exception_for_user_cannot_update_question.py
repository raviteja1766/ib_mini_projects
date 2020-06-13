from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
import pytest
from content_management_portal.constants.exception_messages\
    import USER_CANNOT_UPDATE_QUESTION_EXCEPTION
from django_swagger_utils.drf_server.exceptions import Forbidden

def test_raise_exception_for_cannot_update_question_raises_exception():

    # Arrange
    presenter = PresenterImplementation()
    exception_messages = USER_CANNOT_UPDATE_QUESTION_EXCEPTION[0]

    # Act
    with pytest.raises(Forbidden) as e:
        presenter.raise_exception_for_user_cannot_update_question()

    # Assert
    assert str(e.value) == exception_messages
