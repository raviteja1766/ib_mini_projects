import pytest
from freezegun import freeze_time
from content_management_portal.storages.test_case_storage_implementation\
    import TestCaseStorageImplementation
from content_management_portal.models import TestCase


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_test_case_given_valid_test_case_and_returns_true(
        create_test_cases):

    # Arrange
    test_case_id = 1
    test_case_storage = TestCaseStorageImplementation()
    expected_response = True

    # Act
    actual_response = test_case_storage.validate_test_case(
        test_case_id=test_case_id
    )

    # Assert
    assert actual_response == expected_response

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_test_case_given_invalid_test_case_and_returns_false(
        create_test_cases):

    # Arrange
    test_case_id = 2
    test_case_storage = TestCaseStorageImplementation()
    expected_response = False

    # Act
    actual_response = test_case_storage.validate_test_case(
        test_case_id=test_case_id
    )

    # Assert
    assert actual_response == expected_response
