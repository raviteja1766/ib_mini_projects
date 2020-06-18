import pytest
from typing import List
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions \
    import NotFound, BadRequest, Forbidden
from gyaan.interactors.get_domain_details_interactor \
    import GetDomainDetailsInteractor
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.exceptions.exceptions import DomainDoesNotExist


def test_get_domain_details_interactor_given_invalid_domain_raises_exception():

    # Arrange
    domain_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    storage.validate_domain_id.side_effect = DomainDoesNotExist(domain_id=1)
    interactor = GetDomainDetailsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_exception_for_invalid_domain.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_details_wrapper(
            user_id=user_id, presenter=presenter,
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
    storage = create_autospec(StorageInterface)
    interactor = GetDomainDetailsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = False
    presenter.raise_exception_for_user_not_domain_member\
        .side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.get_domain_details_wrapper(
            user_id=user_id, presenter=presenter,
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


def test_get_domain_details_interactor_given_user_domain_expert_returns_domain_details(
        domain_details_dto, domain_dto, domain_stats, users_dtos,
        join_requests, requested_users
        ):
    # Arrange
    domain_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    interactor = GetDomainDetailsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = True
    storage.get_domain_dto.return_value = domain_dto
    storage.get_domain_stats.return_value = domain_stats
    storage.get_domain_expert_ids.return_value = [user_id]
    storage.get_users_details.side_effect = [users_dtos, requested_users]
    storage.is_user_domain_expert.return_value = True
    storage.get_domain_join_requests.return_value = join_requests

    # Act

    interactor_response = interactor.get_domain_details_wrapper(
        user_id=user_id, presenter=presenter,
        domain_id=domain_id
    )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )
    storage.get_domain_dto.assert_called_once_with(domain_id=domain_id)
    storage.get_domain_stats.assert_called_once_with(domain_id=domain_id)
    storage.get_domain_expert_ids.assert_called_once_with(domain_id=domain_id)
    calls = storage.get_users_details.call_args_list
    storage.get_users_details.assert_has_calls(calls)
    storage.is_user_domain_expert.assert_called_once_with(
        user_id=user_id,domain_id=domain_id
    )
    storage.get_domain_join_requests\
        .assert_called_once_with(domain_id=domain_id)
    presenter.get_response_for_get_domain_details.assert_called_once_with(
        domain_details_dto=domain_details_dto
    )


def test_get_domain_details_interactor_given_user_not_domain_expert_returns_domain_details(
        user_not_domain_expert_details_dto, domain_dto,
        domain_stats, domain_experts
        ):
    # Arrange
    domain_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    interactor = GetDomainDetailsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_following_domain.return_value = True
    storage.get_domain_dto.return_value = domain_dto
    storage.get_domain_stats.return_value = domain_stats
    storage.get_domain_expert_ids.return_value = [2]
    storage.get_users_details.side_effect = [domain_experts, [] ]
    storage.is_user_domain_expert.return_value = False
    storage.get_domain_join_requests.return_value = []

    # Act
    interactor_response = interactor.get_domain_details_wrapper(
        user_id=user_id, presenter=presenter,
        domain_id=domain_id
    )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    storage.is_user_following_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )
    storage.get_domain_dto.assert_called_once_with(domain_id=domain_id)
    storage.get_domain_stats.assert_called_once_with(domain_id=domain_id)
    storage.get_domain_expert_ids.assert_called_once_with(domain_id=domain_id)
    calls = storage.get_users_details.call_args_list
    storage.get_users_details.assert_has_calls(calls)
    storage.is_user_domain_expert.assert_called_once_with(
        user_id=user_id,domain_id=domain_id
    )
    presenter.get_response_for_get_domain_details.assert_called_once_with(
        domain_details_dto=user_not_domain_expert_details_dto
    )