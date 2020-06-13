import pytest
from freezegun import freeze_time
from content_management_portal.storages.hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.models import Hint


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_delete_hint_and_get_hint_order_given_valid_deletes_hint(
        create_hints):

    # Assert
    hint_id = 1
    order_id = 1
    hint_storage = HintStorageImplementation()

    # Act
    response_order_id = hint_storage.delete_hint_and_get_hint_order(
        hint_id=hint_id
    )

    # Assert
    assert Hint.objects.filter(id=hint_id).exists() == False
    assert response_order_id == order_id