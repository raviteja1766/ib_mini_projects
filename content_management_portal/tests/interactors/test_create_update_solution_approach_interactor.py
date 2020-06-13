import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions\
    import NotFound, Forbidden, BadRequest
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .solution_approach_storage_interface\
    import SolutionApproachStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import SolutionApproachDto
from content_management_portal.interactors\
    .create_update_solution_approach_interactor\
    import CreateUpdateSolutionApproachInteractor

def test_create_update_solution_approach_given_invalid_question_returns_exception(
        new_solution_approach_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    solution_approach_storage =\
        create_autospec(SolutionApproachStorageInterface)
    interactor = CreateUpdateSolutionApproachInteractor(
        question_storage=question_storage, presenter=presenter,
        solution_approach_storage=solution_approach_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_solution_approach(
            solution_approach_dto=new_solution_approach_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()

def test_create_update_solution_approach_given_invalid_solution_approach_returns_exception(
        update_solution_approach_dto):

    # Arrange
    question_id = 1
    solution_approach_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    solution_approach_storage =\
        create_autospec(SolutionApproachStorageInterface)
    interactor = CreateUpdateSolutionApproachInteractor(
        question_storage=question_storage, presenter=presenter,
        solution_approach_storage=solution_approach_storage
    )
    question_storage.validate_question_id.return_value = True
    solution_approach_storage.validate_solution_approach.return_value = False
    presenter.raise_exception_for_invalid_solution_approach\
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_solution_approach(
            solution_approach_dto=update_solution_approach_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    solution_approach_storage.validate_solution_approach\
        .assert_called_once_with(solution_approach_id=solution_approach_id)
    presenter.raise_exception_for_invalid_solution_approach\
        .assert_called_once()

def test_create_update_solution_approach_given_different_question_returns_exception(
        update_solution_approach_dto):

    # Arrange
    question_id = 1
    solution_approach_id = 1
    solution_approach_question_id = 2
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    solution_approach_storage =\
        create_autospec(SolutionApproachStorageInterface)
    interactor = CreateUpdateSolutionApproachInteractor(
        question_storage=question_storage, presenter=presenter,
        solution_approach_storage=solution_approach_storage
    )
    question_storage.validate_question_id.return_value = True
    solution_approach_storage.validate_solution_approach.return_value = True
    solution_approach_storage.get_question_to_solution_approach\
        .return_value = solution_approach_question_id
    presenter.raise_exception_for_different_question.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.create_update_solution_approach(
            solution_approach_dto=update_solution_approach_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    solution_approach_storage.validate_solution_approach\
        .assert_called_once_with(solution_approach_id=solution_approach_id)
    solution_approach_storage.get_question_to_solution_approach\
        .assert_called_once_with(solution_approach_id=solution_approach_id)
    presenter.raise_exception_for_different_question.assert_called_once()

def test_create_update_solution_approach_when_solution_approach_exists_returns_exception(
        new_solution_approach_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    solution_approach_storage =\
        create_autospec(SolutionApproachStorageInterface)
    interactor = CreateUpdateSolutionApproachInteractor(
        question_storage=question_storage, presenter=presenter,
        solution_approach_storage=solution_approach_storage
    )
    question_storage.validate_question_id.return_value = True
    solution_approach_storage.check_if_solution_approach_exists\
        .return_value = True
    presenter.raise_exception_for_solution_approach_exists\
        .side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.create_update_solution_approach(
            solution_approach_dto=new_solution_approach_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_solution_approach_exists.assert_called_once()

def test_create_update_solution_approach_given_create_solution_approach_returns_details(
        new_solution_approach_dto, new_solution_approach_dict,
        update_solution_approach_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    solution_approach_storage =\
        create_autospec(SolutionApproachStorageInterface)
    interactor = CreateUpdateSolutionApproachInteractor(
        question_storage=question_storage, presenter=presenter,
        solution_approach_storage=solution_approach_storage
    )
    question_storage.validate_question_id.return_value = True
    solution_approach_storage.check_if_solution_approach_exists\
        .return_value = False
    solution_approach_storage.create_solution_approach\
        .return_value = update_solution_approach_dto
    presenter.get_response_for_create_update_solution_approach\
        .return_value = new_solution_approach_dict

    # Act
    interactor_response = interactor.create_update_solution_approach(
            solution_approach_dto=new_solution_approach_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    solution_approach_storage.create_solution_approach\
        .assert_called_once_with(solution_approach_dto=new_solution_approach_dto)
    presenter.get_response_for_create_update_solution_approach\
        .assert_called_once_with(solution_approach_dto=update_solution_approach_dto)


def test_create_update_solution_approach_given_update_solution_approach_returns_details(
        update_solution_approach_dict, update_solution_approach_dto):

    # Arrange
    question_id = 1
    solution_approach_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    solution_approach_storage =\
        create_autospec(SolutionApproachStorageInterface)
    interactor = CreateUpdateSolutionApproachInteractor(
        question_storage=question_storage, presenter=presenter,
        solution_approach_storage=solution_approach_storage
    )
    question_storage.validate_question_id.return_value = True
    solution_approach_storage.validate_solution_approach.return_value = True
    solution_approach_storage.get_question_to_solution_approach\
        .return_value = question_id
    solution_approach_storage.update_solution_approach\
        .return_value = update_solution_approach_dto
    presenter.get_response_for_create_update_solution_approach\
        .return_value = update_solution_approach_dict

    # Act
    interactor_response = interactor.create_update_solution_approach(
            solution_approach_dto=update_solution_approach_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    solution_approach_storage.update_solution_approach\
        .assert_called_once_with(
            solution_approach_dto=update_solution_approach_dto)
    solution_approach_storage.validate_solution_approach\
        .assert_called_once_with(
            solution_approach_id=solution_approach_id)
    solution_approach_storage.get_question_to_solution_approach\
        .assert_called_once_with(
            solution_approach_id=solution_approach_id)
    presenter.get_response_for_create_update_solution_approach\
        .assert_called_once_with(
            solution_approach_dto=update_solution_approach_dto)

