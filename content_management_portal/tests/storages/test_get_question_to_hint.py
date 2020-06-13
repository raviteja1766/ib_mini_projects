import pytest
from freezegun import freeze_time
from content_management_portal.storages.hint_storage_implementation\
    import HintStorageImplementation

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_question_to_hint_given_hint_returns_question_id(
        create_hints):

    # Assert
    hint_id = 1
    question_id = 1
    hint_storage = HintStorageImplementation()

    # Act
    response_id = hint_storage.get_question_to_hint(
        hint_id=hint_id
    )

    # Assert
    assert response_id == question_id