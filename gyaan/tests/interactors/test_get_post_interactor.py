import pytest
from typing import List
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from gyaan.interactors.get_posts_interactor import GetPostsInteractor
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.dtos import CompletePostDetails


def test_get_posts_interactor_given_duplicate_post_ids_raises_exception():

    # Arrange
    post_ids = [1, 3, 5, 3, 1]
    expected_duplicate_ids = [1, 3]
    storage = create_autospec(StorageInterface)
    interactor = GetPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_exception_for_duplicate_post_ids.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_posts_wrapper(post_ids=post_ids, presenter=presenter)

    # Assert
    presenter_kwargs_dict = \
        presenter.raise_exception_for_duplicate_post_ids.call_args.kwargs
    duplicate_ids_obj = presenter_kwargs_dict['error_obj']
    assert expected_duplicate_ids == duplicate_ids_obj.duplicate_ids

def test_get_posts_interactor_given_invalid_post_ids_raises_exception():

    # Arrange
    post_ids = [1, 2, 3, 4, 5]
    invalid_post_ids = [1, 3]
    storage = create_autospec(StorageInterface)
    storage.get_valid_post_ids.return_value = [2, 4, 5]
    interactor = GetPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_exception_for_invalid_post_ids.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_posts_wrapper(post_ids=post_ids, presenter=presenter)

    # Assert
    presenter_kwargs_dict = \
        presenter.raise_exception_for_invalid_post_ids.call_args.kwargs
    invalid_ids_obj = presenter_kwargs_dict['error_obj']
    assert invalid_post_ids == invalid_ids_obj.post_ids

def test_get_posts_interactor_given_valid_details_returns_complete_post_details(
        post_dtos, post_reaction_counts, comment_reaction_counts,
        posts_tags_dto, comment_counts, reply_counts, users_dtos,
        complete_post_details, comment_dtos
        ):

    # Arrange
    post_ids = [1, 2, 3, 4, 5]
    storage_post_ids = [1, 2, 3, 4, 5]
    comment_ids = [1, 2]
    user_ids = [1]
    storage = create_autospec(StorageInterface)
    storage.get_valid_post_ids.return_value = storage_post_ids
    storage.get_posts_details.return_value = post_dtos
    storage.get_posts_tags.return_value = posts_tags_dto
    storage.get_posts_comments_count.return_value = comment_counts
    storage.get_posts_reactions_count.return_value = post_reaction_counts
    storage.get_latest_comment_ids_to_posts.return_value = comment_ids
    storage.get_comments_details.return_value = comment_dtos
    storage.get_comment_reactions_count.return_value = comment_reaction_counts
    storage.get_comments_replies_count.return_value = reply_counts
    storage.get_user_details.return_value = users_dtos
    interactor = GetPostsInteractor(storage=storage)
    presenter = create_autospec(PresenterInterface)


    # Act
    interactor_response = \
        interactor.get_posts_wrapper(post_ids=post_ids, presenter=presenter)

    # Assert
    storage.get_valid_post_ids.assert_called_once_with(post_ids=post_ids)
    storage.get_posts_details.assert_called_once_with(post_ids=post_ids)
    storage.get_posts_tags.assert_called_once_with(post_ids=post_ids)
    storage.get_posts_comments_count.assert_called_once_with(post_ids=post_ids)
    storage.get_posts_reactions_count.assert_called_once_with(post_ids=post_ids)
    storage.get_latest_comment_ids_to_posts.assert_called_once_with(post_ids=post_ids)
    storage.get_comments_details.assert_called_once_with(comment_ids=comment_ids)
    storage.get_comment_reactions_count.assert_called_once_with(comment_ids=comment_ids)
    storage.get_comments_replies_count.assert_called_once_with(comment_ids=comment_ids)
    storage.get_user_details.assert_called_once_with(user_ids=user_ids)
    assert interactor_response == complete_post_details
