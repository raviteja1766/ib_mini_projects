import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import CleanSolutionDto
from content_management_portal.interactors\
    .create_update_clean_solutions_interactor\
    import CreateUpdateCleanSolutionsInteractor


def test_create_update_clean_solution_given_invalid_question_returns_exception(
        clean_solutions_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    interactor = CreateUpdateCleanSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_clean_solutions(
            question_id=question_id,
            clean_solutions_dto=clean_solutions_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_create_update_clean_solution_given_invalid_clean_solution_returns_exception(
        clean_solutions_dto):

    # Arrange
    question_id = 1
    clean_solution_ids = [1]
    db_clean_solution_ids = [2]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    interactor = CreateUpdateCleanSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )
    question_storage.validate_question_id.return_value = True
    clean_solution_storage.get_database_clean_solution_ids\
        .return_value = db_clean_solution_ids
    presenter.raise_exception_for_invalid_clean_solution.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_clean_solutions(
            question_id=question_id,
            clean_solutions_dto=clean_solutions_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.get_database_clean_solution_ids.assert_called_once_with(
        clean_solution_ids=clean_solution_ids
    )
    presenter.raise_exception_for_invalid_clean_solution.assert_called_once()


def test_create_update_clean_solution_given_different_question_clean_solution_returns_exception(
        clean_solutions_dto):

    # Arrange
    question_id = 1
    clean_solution_ids = [1]
    clean_solution_question_ids = [1,2]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    interactor = CreateUpdateCleanSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )
    question_storage.validate_question_id.return_value = True
    clean_solution_storage.get_database_clean_solution_ids\
        .return_value = clean_solution_ids
    clean_solution_storage.get_clean_solutions_question_ids\
        .return_value = clean_solution_question_ids
    presenter.raise_exception_for_different_question.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.create_update_clean_solutions(
            question_id=question_id,
            clean_solutions_dto=clean_solutions_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.get_database_clean_solution_ids.assert_called_once_with(
        clean_solution_ids=clean_solution_ids
    )
    clean_solution_storage.get_clean_solutions_question_ids.assert_called_once_with(
        clean_solution_ids=clean_solution_ids)
    clean_solution_storage.get_clean_solutions_question_ids.assert_called_once_with(
        clean_solution_ids=clean_solution_ids)
    presenter.raise_exception_for_different_question.assert_called_once()


def test_create_update_clean_solution_given_valid_details_returns_details(
        clean_solutions_dto, new_clean_solutions_dto,
        update_clean_solutions_dto, clean_solutions_dto_response):

    # Arrange
    storage_clean_solutions_dto = [
        CleanSolutionDto(
            id=1, file_name="prime.py", language_type="PYTHON",
            text_code="text code for python", question_id=1, user_id=1
        ),
        CleanSolutionDto(
            id=2, file_name="java.py", language_type="JAVA",
            text_code="text code for java", question_id=1, user_id=1
        )
    ]
    question_id = 1
    clean_solution_ids = [1]
    clean_solution_question_ids = [1]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    clean_solution_storage = create_autospec(CleanSolutionStorageInterface)
    interactor = CreateUpdateCleanSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )
    question_storage.validate_question_id.return_value = True
    clean_solution_storage.get_database_clean_solution_ids\
        .return_value = clean_solution_ids
    clean_solution_storage.get_clean_solutions_question_ids\
        .return_value = clean_solution_question_ids
    clean_solution_storage.get_clean_solutions_to_question\
        .return_value = storage_clean_solutions_dto
    presenter.get_response_for_create_update_clean_solutions\
        .return_value = clean_solutions_dto_response

    # Act
    interactor_response = interactor.create_update_clean_solutions(
        question_id=question_id,
        clean_solutions_dto=clean_solutions_dto
    )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    clean_solution_storage.get_database_clean_solution_ids\
        .assert_called_once_with(clean_solution_ids=clean_solution_ids)
    clean_solution_storage.get_clean_solutions_question_ids\
        .assert_called_once_with(clean_solution_ids=clean_solution_ids)
    clean_solution_storage.get_clean_solutions_question_ids\
        .assert_called_once_with(clean_solution_ids=clean_solution_ids)
    clean_solution_storage.update_clean_solutions.assert_called_once_with(
        question_id=question_id,
        clean_solutions_dto=update_clean_solutions_dto)
    clean_solution_storage.create_clean_solutions.assert_called_once_with(
        clean_solutions_dto=new_clean_solutions_dto)
    presenter.get_response_for_create_update_clean_solutions\
        .assert_called_once_with(
            clean_solutions_dto=storage_clean_solutions_dto
        )
