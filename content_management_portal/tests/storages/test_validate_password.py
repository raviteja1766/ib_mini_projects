from content_management_portal.storages.user_storage_implementation\
    import UserStorageImplementation
import pytest
from content_management_portal.exceptions.exceptions import InvalidPassword


@pytest.mark.django_db
def test_validate_password_to_user_given_valid_details_returns_user_id(
        create_users):

    # Assert
    username = "username1"
    password = "Mdjsfs@713"
    user_storage = UserStorageImplementation()
    expected_user_id = 1

    # Act
    actual_user_id = user_storage.validate_password_to_user(username, password)

    # Assert
    assert expected_user_id == actual_user_id


@pytest.mark.django_db
def test_validate_password_to_user_given_invalid_details_raises_invalidpassword(
        create_users):

    # Assert
    username = "username1"
    password = "Mdjsfs@7shg"
    user_storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidPassword):
        user_storage.validate_password_to_user(
            username=username, password=password
        )
