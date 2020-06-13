import pytest
from freezegun import freeze_time
from content_management_portal.storages.test_case_storage_implementation\
    import TestCaseStorageImplementation

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_question_to_test_case_given_test_case_returns_question_id(
        create_test_cases):

    # Assert
    test_case_id = 1
    question_id = 1
    test_case_storage = TestCaseStorageImplementation()

    # Act
    response_id = test_case_storage.get_question_to_test_case(
        test_case_id=test_case_id
    )

    # Assert
    assert response_id == question_id