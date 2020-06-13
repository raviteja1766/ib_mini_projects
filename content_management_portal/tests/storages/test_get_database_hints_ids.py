import pytest
from content_management_portal.storages\
    .hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.models import Hint


@pytest.mark.django_db
def test_get_hint_ids_given_valid_details_returns_ids(
        create_hints):

    # Arrange
    hint_ids = [1]
    prefilled_storage = HintStorageImplementation()

    # Act
    db_hint_ids = prefilled_storage.get_database_hint_ids(
        hint_ids=hint_ids)

    # Assert
    assert db_hint_ids == hint_ids
