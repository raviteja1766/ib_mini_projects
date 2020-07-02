import pytest
from unittest.mock import create_autospec, patch
from content_management_portal.interactors.get_users_details_interactor \
    import GetQuestionsUserDetailsInteractor
from content_management_portal.storages.question_storage_implementation \
    import QuestionStorageImplementation
from content_management_portal.presenters.presenter_implementation \
    import PresenterImplementation
from content_management_portal.adapters.auth_service \
    import AuthService
from user_app.exceptions.exceptions import DuplicateUserIds, InvalidUserIds



def test_given_duplicate_question_ids_raises_exception():

    # Arrange
    question_ids = [1, 3, 1, 4, 6, 3]
    question_storage = create_autospec(QuestionStorageImplementation)
    interactor = GetQuestionsUserDetailsInteractor(
        question_ids=question_ids, question_storage=question_storage
    )
    presenter = create_autospec(PresenterImplementation)

    # Act
    interactor.get_questions_user_details_wrapper(presenter=presenter)

    # Assert
    presenter.raise_exception_for_duplicate_ids.assert_called_once()

def test_given_invalid_question_ids_raises_exception():

    # Arrange
    question_ids = [1, 2, 3, 4, 5]
    db_question_ids = [1, 2, 3]
    question_storage = create_autospec(QuestionStorageImplementation)
    question_storage.get_valid_question_ids.return_value = db_question_ids
    interactor = GetQuestionsUserDetailsInteractor(
        question_ids=question_ids, question_storage=question_storage
    )
    presenter = create_autospec(PresenterImplementation)

    # Act
    interactor.get_questions_user_details_wrapper(presenter=presenter)

    # Assert
    presenter.raise_exception_for_invalid_question.assert_called_once()

@patch.object(AuthService, 'interface')
def test_given_duplicate_user_ids_raises_exception(mock_adapter):

    # Arrange
    mock_adapter.get_user_dtos.side_effect = DuplicateUserIds(user_ids=[1, 2])
    question_ids = [1, 2, 3, 4, 5]
    db_question_ids = [1, 2, 3, 4, 5]
    user_ids = [1, 2, 1, 3, 2]
    question_storage = create_autospec(QuestionStorageImplementation)
    question_storage.get_valid_question_ids.return_value = db_question_ids
    question_storage.get_user_ids_of_questions.return_value = user_ids
    interactor = GetQuestionsUserDetailsInteractor(
        question_ids=question_ids, question_storage=question_storage
    )
    presenter = create_autospec(PresenterImplementation)

    # Act
    interactor.get_questions_user_details_wrapper(presenter=presenter)

    # Assert
    presenter.raise_exception_for_duplicate_ids.assert_called_once()


@patch.object(AuthService, 'interface')
def test_given_invalid_user_ids_raises_exception(mock_adapter):

    # Arrange
    mock_adapter.get_user_dtos.side_effect = InvalidUserIds(user_ids=[1, 2])
    question_ids = [1, 2, 3, 4, 5]
    db_question_ids = [1, 2, 3, 4, 5]
    user_ids = [1, 2, 3, 4, 5]
    question_storage = create_autospec(QuestionStorageImplementation)
    question_storage.get_valid_question_ids.return_value = db_question_ids
    question_storage.get_user_ids_of_questions.return_value = user_ids
    interactor = GetQuestionsUserDetailsInteractor(
        question_ids=question_ids, question_storage=question_storage
    )
    presenter = create_autospec(PresenterImplementation)

    # Act
    interactor.get_questions_user_details_wrapper(presenter=presenter)

    # Assert
    presenter.raise_exception_for_invalid_user_ids.assert_called_once()

