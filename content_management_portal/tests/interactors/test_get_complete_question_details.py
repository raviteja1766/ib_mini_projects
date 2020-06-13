import pytest
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from unittest.mock import create_autospec
from content_management_portal.interactors\
    .get_complete_question_details_interactor\
    import GetQuestionCompleteDetailsInteractor
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec


def test_delete_question_given_invalid_details_returns_exception():

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = GetQuestionCompleteDetailsInteractor(
        question_storage=question_storage, presenter=presenter
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_complete_question_details(question_id=question_id)

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_get_complete_question_details_given_details_returns_question_details(
        question_complete_details_dto, question_complete_details_dto_response):

    # Arrange
    (
        question_dto, rough_solutions_dto, test_cases_dto,
        prefilled_codes_dto, solution_approach_dto,
        clean_solutions_dto, hints_dto
    ) = question_complete_details_dto
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = GetQuestionCompleteDetailsInteractor(
        question_storage=question_storage, presenter=presenter
    )
    question_storage.validate_question_id.return_value = False
    question_storage.get_complete_question_details_dto.return_value =\
        question_complete_details_dto
    presenter.get_response_for_complete_question_details.return_value =\
        question_complete_details_dto_response

    # Act
    interactor_response = interactor.get_complete_question_details(
        question_id=question_id)

    # Assert
    question_storage.get_complete_question_details_dto\
        .assert_called_once_with(question_id=question_id)
    presenter.get_response_for_complete_question_details\
        .assert_called_once_with(
            question_dto=question_dto,
            rough_solutions_dto=rough_solutions_dto,
            test_cases_dto=test_cases_dto,
            prefilled_codes_dto=prefilled_codes_dto,
            solution_approach_dto=solution_approach_dto,
            clean_solutions_dto=clean_solutions_dto,
            hints_dto=hints_dto
        )
