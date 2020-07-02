
import pytest
from unittest.mock import create_autospec

from user_app.interactors.storages.user_storage_interface\
    import UserStorageInterface
from common.oauth2_storage import OAuth2SQLStorage
from user_app.interactors.get_user_details_interactor\
    import GetUserDetailsInteractor
from user_app.interactors.storages.dtos import UserDto
from user_app.exceptions.exceptions import DuplicateUserIds, InvalidUserIds



def test_get_user_details_given_valid_details_returns_user_details():

    # Arrange
    user_ids = [1, 2]
    user_dtos = [
        UserDto(user_id=1, username="raviteja"),
        UserDto(user_id=2, username="maheshbabu")
    ]
    user_storage = create_autospec(UserStorageInterface)
    user_storage.get_user_details_dtos.return_value = user_dtos
    user_storage.get_valid_user_ids.return_value = user_ids
    interactor = GetUserDetailsInteractor(user_storage=user_storage)

    # Act
    response = interactor.get_user_details_wrapper(user_ids=user_ids)

    # Assert
    assert response == user_dtos
    user_storage.get_user_details_dtos\
        .assert_called_once_with(user_ids=user_ids)
    user_storage.get_valid_user_ids.assert_called_once_with(user_ids=user_ids)

def test_get_user_details_given_duplicate_user_ids_raises_exception():

    # Arrange
    user_ids = [1, 2, 1]
    user_dtos = [
        UserDto(user_id=1, username="raviteja"),
        UserDto(user_id=2, username="maheshbabu")
    ]
    user_storage = create_autospec(UserStorageInterface)
    user_storage.get_user_details_dtos.return_value = user_dtos
    user_storage.get_valid_user_ids.return_value = user_ids
    interactor = GetUserDetailsInteractor(user_storage=user_storage)

    # Act
    with pytest.raises(DuplicateUserIds):
        interactor.get_user_details_wrapper(user_ids=user_ids)

def test_get_user_details_given_invalid_user_ids_raises_exception():

    # Arrange
    user_ids = [1, 2]
    user_dtos = [
        UserDto(user_id=1, username="raviteja"),
        UserDto(user_id=2, username="maheshbabu")
    ]
    user_storage = create_autospec(UserStorageInterface)
    user_storage.get_user_details_dtos.return_value = user_dtos
    user_storage.get_valid_user_ids.return_value = [1]
    interactor = GetUserDetailsInteractor(user_storage=user_storage)

    # Act
    with pytest.raises(InvalidUserIds):
        interactor.get_user_details_wrapper(user_ids=user_ids)

    # Assert
    user_storage.get_valid_user_ids.assert_called_once_with(user_ids=user_ids)
