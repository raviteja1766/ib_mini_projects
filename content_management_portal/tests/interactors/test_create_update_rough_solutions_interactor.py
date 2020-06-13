import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import RoughSolutionDto
from content_management_portal.interactors\
    .create_update_rough_solutions_interactor\
    import CreateUpdateRoughSolutionsInteractor


def test_create_update_rough_solution_given_invalid_question_returns_exception(
        rough_solutions_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    rough_storage = create_autospec(RoughSolutionStorageInterface)
    interactor = CreateUpdateRoughSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_storage=rough_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_rough_solutions(
            question_id=question_id,
            rough_solutions_dto=rough_solutions_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_create_update_rough_solution_given_invalid_rough_solution_returns_exception(
        rough_solutions_dto):

    # Arrange
    question_id = 1
    rough_solution_ids = [1,2]
    db_rough_solution_ids = [2]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    rough_storage = create_autospec(RoughSolutionStorageInterface)
    interactor = CreateUpdateRoughSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_storage=rough_storage
    )
    question_storage.validate_question_id.return_value = True
    rough_storage.get_database_rough_solution_ids\
        .return_value = db_rough_solution_ids
    presenter.raise_exception_for_invalid_rough_solution.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_rough_solutions(
            question_id=question_id,
            rough_solutions_dto=rough_solutions_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_storage.get_database_rough_solution_ids.assert_called_once_with(
        rough_solution_ids=rough_solution_ids
    )
    presenter.raise_exception_for_invalid_rough_solution.assert_called_once()


def test_create_update_rough_solution_given_different_question_rough_solution_returns_exception(
        rough_solutions_dto):

    # Arrange
    question_id = 1
    rough_solution_ids = [1, 2]
    rough_solution_question_ids = [1,2]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    rough_storage = create_autospec(RoughSolutionStorageInterface)
    interactor = CreateUpdateRoughSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_storage=rough_storage
    )
    question_storage.validate_question_id.return_value = True
    rough_storage.get_database_rough_solution_ids\
        .return_value = rough_solution_ids
    rough_storage.get_rough_solutions_question_ids\
        .return_value = rough_solution_question_ids
    presenter.raise_exception_for_different_question.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.create_update_rough_solutions(
            question_id=question_id,
            rough_solutions_dto=rough_solutions_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_storage.get_database_rough_solution_ids.assert_called_once_with(
        rough_solution_ids=rough_solution_ids
    )
    rough_storage.get_rough_solutions_question_ids.assert_called_once_with(
        rough_solution_ids=rough_solution_ids)
    rough_storage.get_rough_solutions_question_ids.assert_called_once_with(
        rough_solution_ids=rough_solution_ids)
    presenter.raise_exception_for_different_question.assert_called_once()


def test_create_update_rough_solution_given_valid_details_returns_details(
        rough_solutions_dto, new_rough_solutions_dto,
        update_rough_solutions_dto, rough_solutions_dto_response):

    # Arrange
    storage_rough_solutions_dto = [
        RoughSolutionDto(
            id=1, file_name="prime.py", language_type="PYTHON",
            text_code="text code for python", question_id=1, user_id=1
        ),
        RoughSolutionDto(
            id=2, file_name="java.py", language_type="JAVA",
            text_code="text code for java", question_id=1, user_id=1
        )
    ]
    question_id = 1
    rough_solution_ids = [1, 2]
    rough_solution_question_ids = [1]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    rough_storage = create_autospec(RoughSolutionStorageInterface)
    interactor = CreateUpdateRoughSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_storage=rough_storage
    )
    question_storage.validate_question_id.return_value = True
    rough_storage.get_database_rough_solution_ids\
        .return_value = rough_solution_ids
    rough_storage.get_rough_solutions_question_ids\
        .return_value = rough_solution_question_ids
    rough_storage.get_rough_solutions_to_question\
        .return_value = storage_rough_solutions_dto
    presenter.get_response_for_create_update_rough_solutions\
        .return_value = rough_solutions_dto_response

    # Act
    interactor_response = interactor.create_update_rough_solutions(
        question_id=question_id,
        rough_solutions_dto=rough_solutions_dto
    )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_storage.get_database_rough_solution_ids\
        .assert_called_once_with(rough_solution_ids=rough_solution_ids)
    rough_storage.get_rough_solutions_question_ids\
        .assert_called_once_with(rough_solution_ids=rough_solution_ids)
    rough_storage.get_rough_solutions_question_ids\
        .assert_called_once_with(rough_solution_ids=rough_solution_ids)
    rough_storage.update_rough_solutions.assert_called_once_with(
        question_id=question_id,
        rough_solutions_dto=rough_solutions_dto)
    presenter.get_response_for_create_update_rough_solutions\
        .assert_called_once_with(
            rough_solutions_dto=storage_rough_solutions_dto
        )


def test_create_update_rough_solution_given_create_details_returns_details(
        new_rough_solutions_dto, update_rough_solutions_dto,
        rough_solutions_dto_response):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    rough_storage = create_autospec(RoughSolutionStorageInterface)
    interactor = CreateUpdateRoughSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_storage=rough_storage
    )
    question_storage.validate_question_id.return_value = True
    rough_storage.get_rough_solutions_to_question\
        .return_value = update_rough_solutions_dto
    presenter.get_response_for_create_update_rough_solutions\
        .return_value = rough_solutions_dto_response

    # Act
    interactor_response = interactor.create_update_rough_solutions(
        question_id=question_id,
        rough_solutions_dto=new_rough_solutions_dto
    )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    rough_storage.create_rough_solutions.assert_called_once_with(
        rough_solutions_dto=new_rough_solutions_dto)
    presenter.get_response_for_create_update_rough_solutions\
        .assert_called_once_with(
            rough_solutions_dto=update_rough_solutions_dto
        )
