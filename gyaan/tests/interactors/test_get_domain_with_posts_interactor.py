import pytest
from typing import List
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions \
    import NotFound, BadRequest, Forbidden
from gyaan.interactors.get_domain_with_posts_interactor \
    import GetDomainWithPostsInteractor
from gyaan.interactors.get_domain_posts_interactor \
    import DomainPostsInteractor
from gyaan.interactors.get_domain_details_interactor \
    import GetDomainDetailsInteractor
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.dtos import CompletePostDetails
from gyaan.exceptions.exceptions import DomainDoesNotExist
from gyaan.interactors.get_posts_interactor import GetPostsInteractor


def test_domain_posts_interactor_given_invalid_domain_raises_exception():

    # Arrange
    domain_id = 1
    user_id = 1
    offset = 1
    limit = 5
    storage = create_autospec(StorageInterface)
    storage.validate_domain_id.side_effect = DomainDoesNotExist(domain_id=1)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_exception_for_invalid_domain.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_with_posts_wrapper(
            user_id=user_id, presenter=presenter,
            offset=offset, limit=limit,
            domain_id=domain_id
        )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    presenter_kwargs_dict = \
        presenter.raise_exception_for_invalid_domain.call_args.kwargs
    domain_obj = presenter_kwargs_dict['error_obj']
    assert domain_id == domain_obj.domain_id

def test_domain_posts_interactor_given_no_member_to_domain_raises_exception():

    # Arrange
    domain_id = 1
    user_id = 1
    offset = 1
    limit = 5
    storage = create_autospec(StorageInterface)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = False
    presenter.raise_exception_for_user_not_domain_member\
        .side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.get_domain_with_posts_wrapper(
            user_id=user_id, presenter=presenter,
            offset=offset, limit=limit,
            domain_id=domain_id
        )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )
    presenter_kwargs_dict = \
        presenter.raise_exception_for_user_not_domain_member.call_args.kwargs
    domain_obj = presenter_kwargs_dict['error_obj']
    assert domain_id == domain_obj.domain_id
    assert user_id == domain_obj.user_id

def test_domain_posts_interactor_given_invalid_offset_raises_exception():

    # Arrange
    domain_id = 1
    user_id = 1
    offset = -1
    limit = 5
    storage = create_autospec(StorageInterface)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = True
    presenter.raise_exception_for_invalid_offset_value\
        .side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_with_posts_wrapper(
            user_id=user_id, presenter=presenter,
            offset=offset, limit=limit,
            domain_id=domain_id
        )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )
    presenter.raise_exception_for_invalid_offset_value.assert_called_once()

def test_domain_posts_interactor_given_invalid_limit_raises_exception():

    # Arrange
    domain_id = 1
    user_id = 1
    offset = 2
    limit = 6
    storage = create_autospec(StorageInterface)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = True
    presenter.raise_exception_for_invalid_limit_value\
        .side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_with_posts_wrapper(
            user_id=user_id, presenter=presenter,
            offset=offset, limit=limit,
            domain_id=domain_id
        )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )
    presenter.raise_exception_for_invalid_limit_value.assert_called_once()

@patch.object(GetDomainDetailsInteractor, 'get_domain_details')
@patch.object(DomainPostsInteractor, 'get_domain_posts')
def test_domain_posts_interactor_given_valid_details_returns_details(
        get_domain_posts, get_domain_details,
        complete_post_details, domain_details_dto,
        domain_with_posts_dto):

    # Arrange
    get_domain_details.return_value = domain_details_dto
    get_domain_posts.return_value = complete_post_details
    domain_id = 1
    user_id = 1
    offset = 2
    limit = 5
    storage = create_autospec(StorageInterface)
    interactor = GetDomainWithPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = True
    

    # Act
    interactor_response = interactor.get_domain_with_posts_wrapper(
            user_id=user_id, presenter=presenter,
            offset=offset, limit=limit,
            domain_id=domain_id
        )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )
    presenter.get_domain_with_posts_response.assert_called_once_with(
        domain_with_posts_dto=domain_with_posts_dto
    )