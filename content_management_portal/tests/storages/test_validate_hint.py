import pytest
from freezegun import freeze_time
from content_management_portal.storages.hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.models import Hint


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_hint_given_valid_hint_and_returns_true(
        create_hints):

    # Arrange
    hint_id = 1
    hint_storage = HintStorageImplementation()
    expected_response = True

    # Act
    actual_response = hint_storage.validate_hint(
        hint_id=hint_id
    )

    # Assert
    assert actual_response == expected_response

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_hint_given_invalid_hint_and_returns_false(
        create_hints):

    # Arrange
    hint_id = 2
    hint_storage = HintStorageImplementation()
    expected_response = False

    # Act
    actual_response = hint_storage.validate_hint(
        hint_id=hint_id
    )

    # Assert
    assert actual_response == expected_response
