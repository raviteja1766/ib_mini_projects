import pytest
from typing import List
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions \
    import NotFound, BadRequest, Forbidden
from gyaan.interactors.get_posts_interactor import GetPostsInteractor
from gyaan.interactors.get_domain_posts_interactor \
    import DomainPostsInteractor
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
    interactor = DomainPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_exception_for_invalid_domain.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_posts_wrapper(
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
    interactor = DomainPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = False
    presenter.raise_exception_for_user_not_domain_member\
        .side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.get_domain_posts_wrapper(
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
    interactor = DomainPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = True
    presenter.raise_exception_for_invalid_offset_value\
        .side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_posts_wrapper(
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
    interactor = DomainPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = True
    presenter.raise_exception_for_invalid_limit_value\
        .side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_domain_posts_wrapper(
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


@patch.object(GetPostsInteractor, 'get_posts')
def test_domain_posts_interactor_given_valid_details_returns_details(
        get_posts, complete_post_details):

    # Arrange
    get_posts.return_value=complete_post_details
    domain_id = 1
    user_id = 1
    offset = 2
    limit = 5
    post_ids = [1, 2, 3]
    storage = create_autospec(StorageInterface)
    interactor = DomainPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = True
    storage.get_domain_post_ids.return_value = post_ids
    

    # Act
    interactor_response = interactor.get_domain_posts_wrapper(
            user_id=user_id, presenter=presenter,
            offset=offset, limit=limit,
            domain_id=domain_id
        )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )
    storage.get_domain_post_ids.assert_called_once_with(
        domain_id=domain_id, offset=offset, limit=limit
    )

