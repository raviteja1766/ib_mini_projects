import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.constants.enums import DescriptionType
from unittest.mock import create_autospec
from content_management_portal.interactors.create_update_question_interactor\
    import CreateUpdateQuestionInteractor
from content_management_portal.interactors.storages.dtos import QuestionDto


def test_update_question_given_valid_details_returns_question_details():

    # Arrange
    user_id = 1
    question_id = 1
    short_text = "for loops"
    text_type = DescriptionType.MARKDOWN.value
    description = "mark down code"
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = CreateUpdateQuestionInteractor(
        question_storage=question_storage, presenter=presenter
    )
    question_dto = QuestionDto(
        id=question_id, short_text=short_text, text_type=text_type,
        description=description, user_id=user_id,
        created_at=datetime.datetime(2012, 1, 13)
    )
    question_dto_dict = {
        "question_id": question_id,
        "short_text": short_text,
        "problem_description": {
            "text_type": text_type,
            "text_description": description
        }
    }
    question_storage.validate_question_id.return_value = True
    question_storage.get_user_to_question.return_value = user_id
    question_storage.update_question.return_value = question_dto
    presenter.get_response_for_question_dto.return_value = question_dto_dict

    # Act
    interactor_response = interactor.create_update_question(
        question_dto=question_dto
    )

    # Assert
    question_storage.update_question.assert_called_once_with(
        question_dto=question_dto
    )
    presenter.get_response_for_question_dto.assert_called_once_with(
        question_dto=question_dto
    )


def test_update_question_given_invalid_details_returns_exception():

    # Arrange
    user_id = 1
    question_id = 1
    short_text = "for loops"
    text_type = DescriptionType.MARKDOWN.value
    description = "mark down code"
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = CreateUpdateQuestionInteractor(
        question_storage=question_storage, presenter=presenter
    )
    question_dto = QuestionDto(
        id=question_id, short_text=short_text, text_type=text_type,
        description=description, user_id=user_id,
        created_at=datetime.datetime(2012, 1, 13)
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound
    # Act
    with pytest.raises(NotFound):
        interactor.create_update_question(question_dto=question_dto)

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_update_question_given_different_user_raises_user_cannot_update_question():

    # Arrange
    user_id = 1
    another_user_id = 2
    question_id = 1
    short_text = "for loops"
    text_type = DescriptionType.MARKDOWN.value
    description = "mark down code"
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = CreateUpdateQuestionInteractor(
        question_storage=question_storage, presenter=presenter
    )
    question_dto = QuestionDto(
        id=question_id, short_text=short_text, text_type=text_type,
        description=description, user_id=user_id,
        created_at=datetime.datetime(2012, 1, 13)
    )
    question_storage.validate_question_id.return_value = True
    question_storage.get_user_to_question.return_value = another_user_id
    presenter.raise_exception_for_user_cannot_update_question\
        .side_effect = Forbidden
    # Act
    with pytest.raises(Forbidden):
        interactor.create_update_question(question_dto=question_dto)

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id)
    question_storage.get_user_to_question.assert_called_once_with(
        question_id=question_id)
    presenter.raise_exception_for_user_cannot_update_question\
        .assert_called_once()


def test_create_question_given_valid_details_returns_question_details():

    # Arrange
    user_id = 1
    question_id = 1
    short_text = "for loops"
    text_type = DescriptionType.MARKDOWN.value
    description = "mark down code"
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = CreateUpdateQuestionInteractor(
        question_storage=question_storage, presenter=presenter
    )
    question_dto = QuestionDto(
        id=None, short_text=short_text, text_type=text_type,
        description=description, user_id=user_id,
        created_at=datetime.datetime(2012, 1, 13)
    )
    created_question_dto = QuestionDto(
        id=1, short_text=short_text, text_type=text_type,
        description=description, user_id=user_id,
        created_at=datetime.datetime(2012, 1, 13)
    )
    question_dto_dict = {
        "question_id": question_id,
        "short_text": short_text,
        "problem_description": {
            "text_type": text_type,
            "text_description": description
        }
    }
    question_storage.create_question.return_value = created_question_dto
    presenter.get_response_for_question_dto.return_value = question_dto_dict

    # Act
    interactor_response = interactor.create_update_question(
        question_dto=question_dto
    )

    # Assert
    question_storage.create_question.assert_called_once_with(
        question_dto=question_dto
    )
    presenter.get_response_for_question_dto.assert_called_once_with(
        question_dto=created_question_dto
    )
    assert interactor_response == question_dto_dict