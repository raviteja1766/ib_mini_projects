import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages\
    .prefilled_code_storage_interface import PrefilledCodeStorageInterface
from content_management_portal.interactors\
    .delete_prefilled_code_interactor import DeletePrefilledCodeInteractor


def test_delete_prefilled_code_given_invalid_details_returns_exception():

    # Arrange
    question_id = 1
    prefilled_code_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    interactor = DeletePrefilledCodeInteractor(
        question_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_prefilled_code_to_question(
            question_id=question_id, prefilled_code_id=prefilled_code_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_delete_question_given_invalid_details_returns_invalid_prefilled_code(
        ):

    # Arrange
    question_id = 1
    prefilled_code_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    interactor = DeletePrefilledCodeInteractor(
        question_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage
    )
    question_storage.validate_question_id.return_value = True
    prefilled_code_storage.validate_prefilled_code.return_value = False
    presenter.raise_exception_for_invalid_prefilled_code\
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_prefilled_code_to_question(
            question_id=question_id, prefilled_code_id=prefilled_code_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.validate_prefilled_code.assert_called_once_with(
        prefilled_code_id=prefilled_code_id
    )
    presenter.raise_exception_for_invalid_prefilled_code.assert_called_once()


def test_delete_question_given_different_question_raises_exception():

    # Arrange
    question_id = 1
    prefilled_code_id = 1
    another_question_id = 2
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    interactor = DeletePrefilledCodeInteractor(
        question_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage
    )
    question_storage.validate_question_id.return_value = True
    prefilled_code_storage.validate_prefilled_code.return_value = True
    prefilled_code_storage.get_question_to_prefilled_code\
        .return_value = another_question_id
    presenter.raise_exception_for_different_question\
        .side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.delete_prefilled_code_to_question(
            question_id=question_id, prefilled_code_id=prefilled_code_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.validate_prefilled_code.assert_called_once_with(
        prefilled_code_id=prefilled_code_id
    )
    prefilled_code_storage.get_question_to_prefilled_code.assert_called_once_with(
        prefilled_code_id=prefilled_code_id)
    presenter.raise_exception_for_different_question\
        .assert_called_once()


def test_delete_question_given_valid_details_deletes_prefilled_code():

    # Arrange
    question_id = 1
    prefilled_code_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    interactor = DeletePrefilledCodeInteractor(
        question_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage
    )
    question_storage.validate_question_id.return_value = True
    prefilled_code_storage.validate_prefilled_code.return_value = True
    prefilled_code_storage.get_question_to_prefilled_code\
        .return_value = question_id

    # Act
    interactor.delete_prefilled_code_to_question(
        question_id=question_id, prefilled_code_id=prefilled_code_id
    )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.validate_prefilled_code.assert_called_once_with(
        prefilled_code_id=prefilled_code_id
    )
    prefilled_code_storage.get_question_to_prefilled_code.assert_called_once_with(
        prefilled_code_id=prefilled_code_id)
    prefilled_code_storage.delete_prefilled_code.assert_called_once_with(
        prefilled_code_id=prefilled_code_id
    )