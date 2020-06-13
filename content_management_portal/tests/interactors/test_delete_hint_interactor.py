import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages\
    .hint_storage_interface import HintStorageInterface
from content_management_portal.interactors\
    .delete_hint_interactor import DeleteHintInteractor


def test_delete_hint_given_invalid_details_returns_exception():

    # Arrange
    question_id = 1
    hint_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = DeleteHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_hint_to_question(
            question_id=question_id, hint_id=hint_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_delete_question_given_invalid_details_returns_invalid_hint(
        ):

    # Arrange
    question_id = 1
    hint_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = DeleteHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = True
    hint_storage.validate_hint.return_value = False
    presenter.raise_exception_for_invalid_hint\
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_hint_to_question(
            question_id=question_id, hint_id=hint_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.validate_hint.assert_called_once_with(
        hint_id=hint_id
    )
    presenter.raise_exception_for_invalid_hint.assert_called_once()


def test_delete_question_given_different_question_raises_exception():

    # Arrange
    question_id = 1
    hint_id = 1
    another_question_id = 2
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = DeleteHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = True
    hint_storage.validate_hint.return_value = True
    hint_storage.get_question_to_hint\
        .return_value = another_question_id
    presenter.raise_exception_for_different_question\
        .side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.delete_hint_to_question(
            question_id=question_id, hint_id=hint_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.validate_hint.assert_called_once_with(
        hint_id=hint_id
    )
    hint_storage.get_question_to_hint.assert_called_once_with(
        hint_id=hint_id)
    presenter.raise_exception_for_different_question\
        .assert_called_once()


def test_delete_question_given_valid_details_deletes_hint():

    # Arrange
    question_id = 1
    hint_id = 1
    order_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = DeleteHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = True
    hint_storage.validate_hint.return_value = True
    hint_storage.get_question_to_hint.return_value = question_id
    hint_storage.delete_hint_and_get_hint_order.return_value = order_id

    # Act
    interactor.delete_hint_to_question(
        question_id=question_id, hint_id=hint_id
    )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.validate_hint.assert_called_once_with(
        hint_id=hint_id
    )
    hint_storage.get_question_to_hint.assert_called_once_with(
        hint_id=hint_id)
    hint_storage.delete_hint_and_get_hint_order.assert_called_once_with(
        hint_id=hint_id
    )
    hint_storage.update_questions_next_hints_order.assert_called_once_with(
        question_id=question_id, order_id=order_id)
