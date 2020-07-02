
import pytest
from freezegun import freeze_time
from user_app.storages.user_storage_implementation\
    import UserStorageImplementation


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_valid_user_ids_given_user_ids_returns_valids_user_ids(
        create_users):

    # Arrange
    storage = UserStorageImplementation()
    user_ids = [1, 2]

    # Act
    user_ids_response = storage.get_valid_user_ids(user_ids=user_ids)

    # Assert
    assert user_ids_response == user_ids

