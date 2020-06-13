from content_management_portal.storages.user_storage_implementation\
    import UserStorageImplementation
import pytest
from freezegun import freeze_time
from datetime import datetime


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_username_given_valid_details_returns_true(create_users):

    # Arrange
    username = "username1"
    user_storage = UserStorageImplementation()                                                                                        
    expected_output = True

    # Act
    actual_output = user_storage.validate_username(username=username)

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_username_given_invalid_details_returns_False(create_users):

    # Arrange
    username = "username3"
    user_storage = UserStorageImplementation()
    expected_output = False

    # Act
    actual_output = user_storage.validate_username(username=username)

    # Assert
    assert expected_output == actual_output
