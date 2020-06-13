import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import TestCaseDto
from content_management_portal.interactors\
    .update_test_cases_order_interactor\
    import UpdateTestCasesOrderInteractor


def test_create_update_test_case_given_invalid_question_returns_exception(
        test_cases_swap_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = UpdateTestCasesOrderInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.update_test_cases_order(
            question_id=question_id,
            test_cases_dto=test_cases_swap_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_create_update_test_case_given_invalid_test_case_returns_exception(
        test_cases_swap_dto):

    # Arrange
    question_id = 1
    test_case_ids = [2,5]
    db_test_case_ids = [2,3]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = UpdateTestCasesOrderInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = True
    test_case_storage.get_database_test_case_ids\
        .return_value = db_test_case_ids
    presenter.raise_exception_for_invalid_test_case.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.update_test_cases_order(
            question_id=question_id,
            test_cases_dto=test_cases_swap_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.get_database_test_case_ids.assert_called_once_with(
        test_case_ids=test_case_ids
    )
    presenter.raise_exception_for_invalid_test_case.assert_called_once()


def test_create_update_test_case_given_different_question_test_case_returns_exception(
        test_cases_swap_dto):

    # Arrange
    question_id = 1
    test_case_ids = [2, 5]
    test_case_question_ids = [2, 5]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = UpdateTestCasesOrderInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = True
    test_case_storage.get_database_test_case_ids\
        .return_value = test_case_ids
    test_case_storage.get_test_cases_question_ids\
        .return_value = test_case_question_ids
    presenter.raise_exception_for_different_question.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.update_test_cases_order(
            question_id=question_id,
            test_cases_dto=test_cases_swap_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.get_database_test_case_ids.assert_called_once_with(
        test_case_ids=test_case_ids
    )
    test_case_storage.get_test_cases_question_ids.assert_called_once_with(
        test_case_ids=test_case_ids)
    presenter.raise_exception_for_different_question.assert_called_once()


def test_create_update_test_case_given_valid_details_returns_details(
        test_cases_swap_dto):

    # Arrange
    question_id = 1
    test_case_ids = [2, 5]
    test_case_question_ids = [1]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = UpdateTestCasesOrderInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = True
    test_case_storage.get_database_test_case_ids\
        .return_value = test_case_ids
    test_case_storage.get_test_cases_question_ids\
        .return_value = test_case_question_ids

    # Act
    interactor_response = interactor.update_test_cases_order(
        question_id=question_id,
        test_cases_dto=test_cases_swap_dto
    )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.get_database_test_case_ids\
        .assert_called_once_with(test_case_ids=test_case_ids)
    test_case_storage.get_test_cases_question_ids\
        .assert_called_once_with(test_case_ids=test_case_ids)
    test_case_storage.update_test_cases_order.assert_called_once_with(
        test_cases_dto=test_cases_swap_dto)
