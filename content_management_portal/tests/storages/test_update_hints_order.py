from content_management_portal.storages\
    .hint_storage_implementation\
    import HintStorageImplementation
import pytest
from content_management_portal.models import Hint

@pytest.mark.django_db
def test_validate_update_hint_given_valid_details_returns_ids(
        create_hints, update_hints_swap_dto):

    # Arrange
    hint_id = 1
    order_id = 3
    prefilled_storage = HintStorageImplementation()

    # Act
    prefilled_storage.update_hints_order(
        hints_dto=update_hints_swap_dto
    )

    # Assert
    prefilled_obj = Hint.objects.get(id=hint_id)
    assert prefilled_obj.order_id == order_id