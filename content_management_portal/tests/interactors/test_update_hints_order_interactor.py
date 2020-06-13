import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import HintDto
from content_management_portal.interactors\
    .update_hints_order_interactor\
    import UpdateHintsOrderInteractor


def test_create_update_hint_given_invalid_question_returns_exception(
        hints_swap_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = UpdateHintsOrderInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.update_hints_order(
            question_id=question_id,
            hints_dto=hints_swap_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_create_update_hint_given_invalid_hint_returns_exception(
        hints_swap_dto):

    # Arrange
    question_id = 1
    hint_ids = [2,5]
    db_hint_ids = [2,3]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = UpdateHintsOrderInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = True
    hint_storage.get_database_hint_ids\
        .return_value = db_hint_ids
    presenter.raise_exception_for_invalid_hint.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.update_hints_order(
            question_id=question_id,
            hints_dto=hints_swap_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.get_database_hint_ids.assert_called_once_with(
        hint_ids=hint_ids
    )
    presenter.raise_exception_for_invalid_hint.assert_called_once()


def test_create_update_hint_given_different_question_hint_returns_exception(
        hints_swap_dto):

    # Arrange
    question_id = 1
    hint_ids = [2, 5]
    hint_question_ids = [2, 5]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = UpdateHintsOrderInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = True
    hint_storage.get_database_hint_ids\
        .return_value = hint_ids
    hint_storage.get_hints_question_ids\
        .return_value = hint_question_ids
    presenter.raise_exception_for_different_question.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.update_hints_order(
            question_id=question_id,
            hints_dto=hints_swap_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.get_database_hint_ids.assert_called_once_with(
        hint_ids=hint_ids
    )
    hint_storage.get_hints_question_ids.assert_called_once_with(
        hint_ids=hint_ids)
    presenter.raise_exception_for_different_question.assert_called_once()


def test_create_update_hint_given_valid_details_returns_details(
        hints_swap_dto):

    # Arrange
    question_id = 1
    hint_ids = [2, 5]
    hint_question_ids = [1]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = UpdateHintsOrderInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = True
    hint_storage.get_database_hint_ids\
        .return_value = hint_ids
    hint_storage.get_hints_question_ids\
        .return_value = hint_question_ids

    # Act
    interactor_response = interactor.update_hints_order(
        question_id=question_id,
        hints_dto=hints_swap_dto
    )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.get_database_hint_ids\
        .assert_called_once_with(hint_ids=hint_ids)
    hint_storage.get_hints_question_ids\
        .assert_called_once_with(hint_ids=hint_ids)
    hint_storage.update_hints_order.assert_called_once_with(
        hints_dto=hints_swap_dto)
