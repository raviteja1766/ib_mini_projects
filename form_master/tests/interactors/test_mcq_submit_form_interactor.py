import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from unittest.mock import create_autospec
from form_master.interactors.mcq_submit_form_interactor \
    import MCQQuestionSubmitFormResponseInteractor
from form_master.interactors.storages.storage_interface \
    import StorageInterface
from form_master.interactors.presenters.presenter_interface \
    import PresenterInterface
from form_master.exceptions.exceptions import (
    FormDoesNotExist, QuestionDoesNotBelongToForm
)



def test_mcq_submit_form_interactor_given_invalid_form_raises_exception():

    # Arrange
    form_id = 1
    user_id = 1
    question_id = 1
    option_id = 1
    storage = create_autospec(StorageInterface)
    interactor = MCQQuestionSubmitFormResponseInteractor(
        user_id=user_id, form_id=form_id,
        question_id=question_id, storage=storage,
        user_submitted_option_id=option_id
    )
    storage.get_form_status_dto.side_effect = FormDoesNotExist(form_id=1)
    presenter = create_autospec(PresenterInterface)
    presenter.raise_form_does_not_exist_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Arrange
    dict_obj = presenter.raise_form_does_not_exist_exception.call_args.kwargs
    actual_form_id = dict_obj['error_object'].form_id
    assert actual_form_id == form_id


def test_mcq_submit_form_interactor_given_form_status_closed_form_raises_exception(
        form_status_false):

    # Arrange
    form_id = 1
    user_id = 1
    question_id = 1
    option_id = 1
    storage = create_autospec(StorageInterface)
    interactor = MCQQuestionSubmitFormResponseInteractor(
        user_id=user_id, form_id=form_id,
        question_id=question_id, storage=storage,
        user_submitted_option_id=option_id
    )
    storage.get_form_status_dto.return_value = form_status_false
    presenter = create_autospec(PresenterInterface)
    presenter.raise_form_closed_exception.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Arrange
    storage.get_form_status_dto.assert_called_once_with(form_id=form_id)
    presenter.raise_form_closed_exception.assert_called_once()

def test_mcq_submit_form_interactor_given_form_status_live_form_raises_exception(
        form_status_true):

    # Arrange
    form_id = 1
    user_id = 1
    question_id = 1
    option_id = 1
    storage = create_autospec(StorageInterface)
    interactor = MCQQuestionSubmitFormResponseInteractor(
        user_id=user_id, form_id=form_id,
        question_id=question_id, storage=storage,
        user_submitted_option_id=option_id
    )
    storage.get_form_status_dto.return_value = form_status_true
    presenter = create_autospec(PresenterInterface)
    storage.validate_question_id_with_form\
        .side_effect = QuestionDoesNotBelongToForm
    presenter.raise_question_does_not_belong_to_form_exception\
        .side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Arrange
    storage.get_form_status_dto.assert_called_once_with(form_id=form_id)
    storage.validate_question_id_with_form.assert_called_once_with(
        form_id=form_id, question_id=question_id
    )
    presenter.raise_question_does_not_belong_to_form_exception\
        .assert_called_once()

def test_mcq_submit_form_interactor_given_invalid_user_response_form_raises_exception(
        form_status_true):

    # Arrange
    form_id = 1
    user_id = 1
    question_id = 1
    option_id = 1
    option_ids = [2, 3, 4]
    storage = create_autospec(StorageInterface)
    interactor = MCQQuestionSubmitFormResponseInteractor(
        user_id=user_id, form_id=form_id,
        question_id=question_id, storage=storage,
        user_submitted_option_id=option_id
    )
    storage.get_form_status_dto.return_value = form_status_true
    storage.get_option_ids_for_question.return_value = option_ids
    presenter = create_autospec(PresenterInterface)
    storage.validate_question_id_with_form\
        .return_value = None
    presenter.raise_invalid_user_response_submitted.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Arrange
    storage.get_form_status_dto.assert_called_once_with(form_id=form_id)
    storage.validate_question_id_with_form.assert_called_once_with(
        form_id=form_id, question_id=question_id
    )
    storage.get_option_ids_for_question.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_invalid_user_response_submitted.assert_called_once()

def test_mcq_submit_form_interactor_given_valid_details_returns_response(
        form_status_true, user_response_dto):

    # Arrange
    form_id = 1
    user_id = 1
    question_id = 1
    response_id = 1
    option_id = 1
    option_ids = [2, 1, 4]
    storage = create_autospec(StorageInterface)
    interactor = MCQQuestionSubmitFormResponseInteractor(
        user_id=user_id, form_id=form_id,
        question_id=question_id, storage=storage,
        user_submitted_option_id=option_id
    )
    storage.get_form_status_dto.return_value = form_status_true
    storage.get_option_ids_for_question.return_value = option_ids
    presenter = create_autospec(PresenterInterface)
    storage.validate_question_id_with_form\
        .return_value = None
    storage.create_user_mcq_response.return_value = user_response_dto
    presenter.raise_invalid_user_response_submitted.side_effect = NotFound

    # Act
    interactor_response = interactor.submit_form_response_wrapper(
        presenter=presenter
    )

    # Arrange
    storage.get_form_status_dto.assert_called_once_with(form_id=form_id)
    storage.validate_question_id_with_form.assert_called_once_with(
        form_id=form_id, question_id=question_id
    )
    storage.get_option_ids_for_question.assert_called_once_with(
        question_id=question_id
    )
    storage.create_user_mcq_response.assert_called_once_with(
        user_response_dto=user_response_dto
    )