import pytest
from content_management_portal.storages\
    .hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.models import Hint


@pytest.mark.django_db
def test_get_hints_question_ids_given_valid_details_returns_ids(
        create_hints):

    # Arrange
    hint_ids = [1]
    question_ids = [1]
    hint_storage = HintStorageImplementation()

    # Act
    db_question_ids = hint_storage.get_hints_question_ids(
        hint_ids=hint_ids
    )

    # Assert
    assert db_question_ids == question_ids
