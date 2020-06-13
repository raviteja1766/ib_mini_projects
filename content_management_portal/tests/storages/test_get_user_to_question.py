from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
import pytest
from freezegun import freeze_time
from datetime import datetime


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_user_to_question_returns_user_id(create_questions):

    # Arrange
    user_id = 1
    question_id = 1
    question_storage = QuestionStorageImplementation()

    # Act
    actual_user_id = question_storage.get_user_to_question(
        question_id=question_id)

    # Assert
    assert actual_user_id == user_id
