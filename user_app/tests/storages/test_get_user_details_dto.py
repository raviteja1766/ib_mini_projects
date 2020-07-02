

import pytest
from freezegun import freeze_time
from user_app.storages.user_storage_implementation\
    import UserStorageImplementation
from user_app.interactors.storages.dtos import UserDto


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_user_details_dto_given_user_ids_returns_user_details(
        create_users):

    # Arrange
    storage = UserStorageImplementation()
    user_ids = [1, 2]
    user_dtos = [
        UserDto(user_id=1, username="username1"),
        UserDto(user_id=2, username="username2")
    ]

    # Act
    user_dtos_response = storage.get_user_details_dtos(user_ids=user_ids)

    # Assert
    assert user_dtos_response == user_dtos

