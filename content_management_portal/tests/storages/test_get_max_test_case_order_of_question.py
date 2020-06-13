import pytest
from freezegun import freeze_time
from content_management_portal.storages.test_case_storage_implementation\
    import TestCaseStorageImplementation
from content_management_portal.models import TestCase
from content_management_portal.constants.enums import DescriptionType


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_max_test_case_order_given_question_id_returns_order_id(
        create_test_cases):

    # Arrange
    order_id = 1
    question_id = 1
    test_case_storage = TestCaseStorageImplementation()

    # Act
    storage_response = test_case_storage\
        .get_max_test_case_order_of_question(question_id=question_id)

    # Assert
    assert storage_response == order_id


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_max_test_case_order_given_question_id_test_case_not_exists_returns_none(
        create_questions):

    # Arrange
    order_id = None
    question_id = 1
    test_case_storage = TestCaseStorageImplementation()

    # Act
    storage_response = test_case_storage\
        .get_max_test_case_order_of_question(question_id=question_id)

    # Assert
    assert storage_response == order_id
