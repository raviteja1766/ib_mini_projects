import pytest
from freezegun import freeze_time
from user_app.storages.user_storage_implementation\
    import UserStorageImplementation
from user_app.exceptions.exceptions import InvalidUsername


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_username_given_valid_details_returns_None(create_users):

    # Arrange
    username = "username1"
    user_storage = UserStorageImplementation()                                                                                        
    expected_output = None

    # Act
    actual_output = user_storage.validate_username(username=username)

    # Assert
    assert expected_output == actual_output


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_username_given_invalid_details_raises_exception(create_users):

    # Arrange
    username = "username3"
    user_storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidUsername):
        user_storage.validate_username(username=username)
