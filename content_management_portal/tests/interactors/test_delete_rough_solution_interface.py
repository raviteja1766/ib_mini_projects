import pytest
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages\
    .rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.interactors\
    .delete_rough_solution_interactor import DeleteRoughSolutionInteractor
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden


def test_delete_question_given_invalid_details_returns_exception():

    # Arrange
    question_id = 1
    rough_solution_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    rough_storage = create_autospec(RoughSolutionStorageInterface)
    interactor = DeleteRoughSolutionInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_storage=rough_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound
    # Act
    with pytest.raises(NotFound):
        interactor.delete_rough_solution_to_question(
            question_id=question_id, rough_solution_id=rough_solution_id)

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_delete_question_given_invalid_details_returns_invalid_rough_solution(
        ):

    # Arrange
    question_id = 1
    rough_solution_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    rough_storage = create_autospec(RoughSolutionStorageInterface)
    interactor = DeleteRoughSolutionInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_storage=rough_storage
    )
    question_storage.validate_question_id.return_value = True
    rough_storage.validate_rough_solution_id.return_value = False
    presenter.raise_exception_for_invalid_rough_solution\
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_rough_solution_to_question(
            question_id=question_id, rough_solution_id=rough_solution_id)

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_storage.validate_rough_solution_id.assert_called_once_with(
        rough_solution_id=rough_solution_id
    )
    presenter.raise_exception_for_invalid_rough_solution.assert_called_once()


def test_delete_question_given_rough_solution_to_different_question_raises_exception():

    # Arrange
    question_id = 1
    rough_solution_id = 1
    another_question_id = 2
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    rough_storage = create_autospec(RoughSolutionStorageInterface)
    interactor = DeleteRoughSolutionInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_storage=rough_storage
    )
    question_storage.validate_question_id.return_value = True
    rough_storage.validate_rough_solution_id.return_value = True
    rough_storage.get_question_to_rough_solution\
        .return_value = another_question_id
    presenter.raise_exception_for_rough_solution_not_in_question\
        .side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.delete_rough_solution_to_question(
            question_id=question_id, rough_solution_id=rough_solution_id)

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_storage.validate_rough_solution_id.assert_called_once_with(
        rough_solution_id=rough_solution_id
    )
    rough_storage.get_question_to_rough_solution.assert_called_once_with(
        rough_solution_id=rough_solution_id)
    presenter.raise_exception_for_rough_solution_not_in_question\
        .assert_called_once()


def test_delete_question_given_valid_details_deletes_rough_solution():

    # Arrange
    question_id = 1
    rough_solution_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    rough_storage = create_autospec(RoughSolutionStorageInterface)
    interactor = DeleteRoughSolutionInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_storage=rough_storage
    )
    question_storage.validate_question_id.return_value = True
    rough_storage.validate_rough_solution_id.return_value = True
    rough_storage.get_question_to_rough_solution\
        .return_value = rough_solution_id
    presenter.raise_exception_for_rough_solution_not_in_question\
        .side_effect = Forbidden

    # Act
    interactor.delete_rough_solution_to_question(
        question_id=question_id, rough_solution_id=rough_solution_id)

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_storage.validate_rough_solution_id.assert_called_once_with(
        rough_solution_id=rough_solution_id
    )
    rough_storage.get_question_to_rough_solution.assert_called_once_with(
        rough_solution_id=rough_solution_id)
    rough_storage.delete_rough_solution\
        .assert_called_once_with(rough_solution_id=rough_solution_id)
