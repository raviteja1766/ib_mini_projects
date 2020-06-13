import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages\
    .test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors\
    .delete_test_case_interactor import DeleteTestCaseInteractor


def test_delete_test_case_given_invalid_details_returns_exception():

    # Arrange
    question_id = 1
    test_case_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = DeleteTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_test_case_to_question(
            question_id=question_id, test_case_id=test_case_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_delete_question_given_invalid_details_returns_invalid_test_case(
        ):

    # Arrange
    question_id = 1
    test_case_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = DeleteTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = True
    test_case_storage.validate_test_case.return_value = False
    presenter.raise_exception_for_invalid_test_case\
        .side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.delete_test_case_to_question(
            question_id=question_id, test_case_id=test_case_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.validate_test_case.assert_called_once_with(
        test_case_id=test_case_id
    )
    presenter.raise_exception_for_invalid_test_case.assert_called_once()


def test_delete_question_given_different_question_raises_exception():

    # Arrange
    question_id = 1
    test_case_id = 1
    another_question_id = 2
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = DeleteTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = True
    test_case_storage.validate_test_case.return_value = True
    test_case_storage.get_question_to_test_case\
        .return_value = another_question_id
    presenter.raise_exception_for_different_question\
        .side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.delete_test_case_to_question(
            question_id=question_id, test_case_id=test_case_id
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.validate_test_case.assert_called_once_with(
        test_case_id=test_case_id
    )
    test_case_storage.get_question_to_test_case.assert_called_once_with(
        test_case_id=test_case_id)
    presenter.raise_exception_for_different_question\
        .assert_called_once()


def test_delete_question_given_valid_details_deletes_test_case():

    # Arrange
    question_id = 1
    test_case_id = 1
    order_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = DeleteTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = True
    test_case_storage.validate_test_case.return_value = True
    test_case_storage.get_question_to_test_case\
        .return_value = question_id
    test_case_storage.delete_test_case_and_get_test_case_order\
        .return_value = order_id

    # Act
    interactor.delete_test_case_to_question(
        question_id=question_id, test_case_id=test_case_id
    )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.validate_test_case.assert_called_once_with(
        test_case_id=test_case_id
    )
    test_case_storage.get_question_to_test_case.assert_called_once_with(
        test_case_id=test_case_id)
    test_case_storage.delete_test_case_and_get_test_case_order\
        .assert_called_once_with(test_case_id=test_case_id)
    test_case_storage.update_questions_next_test_cases_order\
        .assert_called_once_with(question_id=question_id, order_id=order_id)
