import pytest
from content_management_portal.storages\
    .test_case_storage_implementation\
    import TestCaseStorageImplementation
from content_management_portal.models import TestCase


@pytest.mark.django_db
def test_get_test_case_ids_given_valid_details_returns_ids(
        create_test_cases):

    # Arrange
    test_case_ids = [1]
    prefilled_storage = TestCaseStorageImplementation()

    # Act
    db_test_case_ids = prefilled_storage.get_database_test_case_ids(
        test_case_ids=test_case_ids)

    # Assert
    assert db_test_case_ids == test_case_ids
