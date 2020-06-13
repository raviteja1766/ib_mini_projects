import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages\
    .clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors\
    .delete_clean_solution_interactor import DeleteCleanSolutionInteractor


def test_delete_clean_solution_given_invalid_details_returns_exception():

    # Arrange
    question_id = 1
    clean_solution_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    interactor = DeleteCleanSolutionInteractor(
        question_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_clean_solution_to_question(
            question_id=question_id, clean_solution_id=clean_solution_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_delete_question_given_invalid_details_returns_invalid_clean_solution(
        ):

    # Arrange
    question_id = 1
    clean_solution_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    interactor = DeleteCleanSolutionInteractor(
        question_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )
    question_storage.validate_question_id.return_value = True
    clean_solution_storage.validate_clean_solution.return_value = False
    presenter.raise_exception_for_invalid_clean_solution\
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_clean_solution_to_question(
            question_id=question_id, clean_solution_id=clean_solution_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.validate_clean_solution.assert_called_once_with(
        clean_solution_id=clean_solution_id
    )
    presenter.raise_exception_for_invalid_clean_solution.assert_called_once()


def test_delete_question_given_different_question_raises_exception():

    # Arrange
    question_id = 1
    clean_solution_id = 1
    another_question_id = 2
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    interactor = DeleteCleanSolutionInteractor(
        question_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )
    question_storage.validate_question_id.return_value = True
    clean_solution_storage.validate_clean_solution.return_value = True
    clean_solution_storage.get_question_to_clean_solution\
        .return_value = another_question_id
    presenter.raise_exception_for_different_question\
        .side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.delete_clean_solution_to_question(
            question_id=question_id, clean_solution_id=clean_solution_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.validate_clean_solution.assert_called_once_with(
        clean_solution_id=clean_solution_id
    )
    clean_solution_storage.get_question_to_clean_solution.assert_called_once_with(
        clean_solution_id=clean_solution_id)
    presenter.raise_exception_for_different_question\
        .assert_called_once()


def test_delete_question_given_valid_details_deletes_clean_solution():

    # Arrange
    question_id = 1
    clean_solution_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    interactor = DeleteCleanSolutionInteractor(
        question_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )
    question_storage.validate_question_id.return_value = True
    clean_solution_storage.validate_clean_solution.return_value = True
    clean_solution_storage.get_question_to_clean_solution\
        .return_value = question_id

    # Act
    interactor.delete_clean_solution_to_question(
        question_id=question_id, clean_solution_id=clean_solution_id
    )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.validate_clean_solution.assert_called_once_with(
        clean_solution_id=clean_solution_id
    )
    clean_solution_storage.get_question_to_clean_solution.assert_called_once_with(
        clean_solution_id=clean_solution_id)
    clean_solution_storage.delete_clean_solution.assert_called_once_with(
        clean_solution_id=clean_solution_id
    )