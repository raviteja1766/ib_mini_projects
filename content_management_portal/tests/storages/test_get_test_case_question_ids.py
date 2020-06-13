import pytest
from content_management_portal.storages\
    .test_case_storage_implementation\
    import TestCaseStorageImplementation
from content_management_portal.models import TestCase


@pytest.mark.django_db
def test_get_test_cases_question_ids_given_valid_details_returns_ids(
        create_test_cases):

    # Arrange
    test_case_ids = [1]
    question_ids = [1]
    test_case_storage = TestCaseStorageImplementation()

    # Act
    db_question_ids = test_case_storage.get_test_cases_question_ids(
        test_case_ids=test_case_ids
    )

    # Assert
    assert db_question_ids == question_ids
