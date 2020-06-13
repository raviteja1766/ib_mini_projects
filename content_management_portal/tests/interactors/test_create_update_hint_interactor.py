import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos import HintDto
from content_management_portal.interactors.create_update_hint_interactor\
    import CreateUpdateHintInteractor

def test_create_update_hint_given_invalid_question_returns_exception(
        new_hint_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = CreateUpdateHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_hint(
            hint_dto=new_hint_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()

def test_create_update_hint_given_invalid_hint_returns_exception(
        update_hint_dto):

    # Arrange
    question_id = 1
    hint_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = CreateUpdateHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = True
    hint_storage.validate_hint.return_value = False
    presenter.raise_exception_for_invalid_hint.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_hint(
            hint_dto=update_hint_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.validate_hint.assert_called_once_with(
        hint_id=hint_id
    )
    presenter.raise_exception_for_invalid_hint.assert_called_once()

def test_create_update_hint_given_different_question_returns_exception(
        update_hint_dto):

    # Arrange
    question_id = 1
    hint_id = 1
    hint_question_id = 2
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = CreateUpdateHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = True
    hint_storage.validate_hint.return_value = True
    hint_storage.get_question_to_hint.return_value = hint_question_id
    presenter.raise_exception_for_different_question.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.create_update_hint(
            hint_dto=update_hint_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.validate_hint.assert_called_once_with(
        hint_id=hint_id
    )
    hint_storage.get_question_to_hint.assert_called_once_with(
        hint_id=hint_id
    )
    presenter.raise_exception_for_different_question.assert_called_once()


def test_create_update_hint_given_create_hint_returns_details(
        new_hint_dto, new_hint_dict, update_hint_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = CreateUpdateHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = True
    hint_storage.get_max_hint_order_of_question.return_value = 1
    hint_storage.create_hint.return_value = update_hint_dto
    presenter.get_response_for_create_update_hint\
        .return_value = new_hint_dict

    # Act
    interactor_response = interactor.create_update_hint(
            hint_dto=new_hint_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.get_max_hint_order_of_question\
        .assert_called_once_with(question_id=question_id)
    hint_storage.create_hint\
        .assert_called_once_with(hint_dto=new_hint_dto)
    presenter.get_response_for_create_update_hint\
        .assert_called_once_with(hint_dto=update_hint_dto)


def test_create_update_hint_given_update_hint_returns_details(
        update_hint_dict, update_hint_dto):

    # Arrange
    question_id = 1
    hint_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    hint_storage = create_autospec(HintStorageInterface)
    interactor = CreateUpdateHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )
    question_storage.validate_question_id.return_value = True
    hint_storage.validate_hint.return_value = True
    hint_storage.get_question_to_hint.return_value = question_id
    hint_storage.update_hint.return_value = update_hint_dto
    presenter.get_response_for_create_update_hint\
        .return_value = update_hint_dict

    # Act
    interactor_response = interactor.create_update_hint(
            hint_dto=update_hint_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    hint_storage.update_hint.assert_called_once_with(hint_dto=update_hint_dto)
    hint_storage.validate_hint.assert_called_once_with(hint_id=hint_id)
    hint_storage.get_question_to_hint.assert_called_once_with(hint_id=hint_id)
    presenter.get_response_for_create_update_hint\
        .assert_called_once_with(hint_dto=update_hint_dto)

