from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
import pytest
from freezegun import freeze_time
from datetime import datetime


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_question_given_valid_details_returns_true(create_questions):

    # Arrange
    question_id = 1
    question_storage = QuestionStorageImplementation()
    expected_output = True

    # Act
    actual_output = question_storage.validate_question_id(question_id)

    # Assert
    assert actual_output == expected_output


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_question_given_invalid_details_returns_false(
        create_questions):

    # Arrange
    question_id = 2
    question_storage = QuestionStorageImplementation()
    expected_output = False

    # Act
    actual_output = question_storage.validate_question_id(question_id)

    # Assert
    assert actual_output == expected_output
