from content_management_portal.storages\
    .test_case_storage_implementation\
    import TestCaseStorageImplementation
import pytest
from content_management_portal.models import TestCase

@pytest.mark.django_db
def test_validate_update_test_case_given_valid_details_returns_ids(
        create_test_cases, update_test_cases_swap_dto):

    # Arrange
    test_case_id = 1
    order_id = 3
    prefilled_storage = TestCaseStorageImplementation()

    # Act
    prefilled_storage.update_test_cases_order(
        test_cases_dto=update_test_cases_swap_dto
    )

    # Assert
    prefilled_obj = TestCase.objects.get(id=test_case_id)
    assert prefilled_obj.order_id == order_id