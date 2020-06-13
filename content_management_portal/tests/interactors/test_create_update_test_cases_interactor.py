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
    .create_update_test_case_interactor\
    import CreateUpdateTestCaseInteractor

def test_create_update_test_case_given_invalid_question_returns_exception(
        new_test_case_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = CreateUpdateTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_test_case(
            test_case_dto=new_test_case_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()

def test_create_update_test_case_given_invalid_test_case_returns_exception(
        update_test_case_dto):

    # Arrange
    question_id = 1
    test_case_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = CreateUpdateTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = True
    test_case_storage.validate_test_case.return_value = False
    presenter.raise_exception_for_invalid_test_case.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_test_case(
            test_case_dto=update_test_case_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.validate_test_case.assert_called_once_with(
        test_case_id=test_case_id
    )
    presenter.raise_exception_for_invalid_test_case.assert_called_once()

def test_create_update_test_case_given_different_question_returns_exception(
        update_test_case_dto):

    # Arrange
    question_id = 1
    test_case_id = 1
    test_case_question_id = 2
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = CreateUpdateTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = True
    test_case_storage.validate_test_case.return_value = True
    test_case_storage.get_question_to_test_case\
        .return_value = test_case_question_id
    presenter.raise_exception_for_different_question.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.create_update_test_case(
            test_case_dto=update_test_case_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.validate_test_case.assert_called_once_with(
        test_case_id=test_case_id
    )
    test_case_storage.get_question_to_test_case.assert_called_once_with(
        test_case_id=test_case_id
    )
    presenter.raise_exception_for_different_question.assert_called_once()


def test_create_update_test_case_given_create_test_case_returns_details(
        new_test_case_dto, new_test_case_dict, update_test_case_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = CreateUpdateTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = True
    test_case_storage.get_max_test_case_order_of_question.return_value = 1
    test_case_storage.create_test_case.return_value = update_test_case_dto
    presenter.get_response_for_create_update_test_case\
        .return_value = new_test_case_dict

    # Act
    interactor_response = interactor.create_update_test_case(
            test_case_dto=new_test_case_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.get_max_test_case_order_of_question\
        .assert_called_once_with(question_id=question_id)
    test_case_storage.create_test_case\
        .assert_called_once_with(test_case_dto=new_test_case_dto)
    presenter.get_response_for_create_update_test_case\
        .assert_called_once_with(test_case_dto=update_test_case_dto)


def test_create_update_test_case_given_update_test_case_returns_details(
        update_test_case_dict, update_test_case_dto):

    # Arrange
    question_id = 1
    test_case_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    test_case_storage = create_autospec(TestCaseStorageInterface)
    interactor = CreateUpdateTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )
    question_storage.validate_question_id.return_value = True
    test_case_storage.validate_test_case.return_value = True
    test_case_storage.get_question_to_test_case\
        .return_value = question_id
    test_case_storage.update_test_case.return_value = update_test_case_dto
    presenter.get_response_for_create_update_test_case\
        .return_value = update_test_case_dict

    # Act
    interactor_response = interactor.create_update_test_case(
            test_case_dto=update_test_case_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    test_case_storage.update_test_case\
        .assert_called_once_with(test_case_dto=update_test_case_dto)
    test_case_storage.validate_test_case\
        .assert_called_once_with(test_case_id=test_case_id)
    test_case_storage.get_question_to_test_case\
        .assert_called_once_with(test_case_id=test_case_id)
    presenter.get_response_for_create_update_test_case\
        .assert_called_once_with(test_case_dto=update_test_case_dto)

