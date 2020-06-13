import pytest
from freezegun import freeze_time
from content_management_portal.storages.test_case_storage_implementation\
    import TestCaseStorageImplementation
from content_management_portal.models import TestCase


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_delete_test_case_given_valid_deletes_test_case(create_test_cases):

    # Assert
    test_case_id = 1
    order_id = 1
    test_case_storage = TestCaseStorageImplementation()

    # Act
    response_id = test_case_storage.delete_test_case_and_get_test_case_order(
        test_case_id=test_case_id
    )

    # Assert
    assert TestCase.objects.filter(id=test_case_id).exists() == False
    assert response_id == order_id