import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .prefilled_code_storage_interface import PrefilledCodeStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import PrefilledCodeDto
from content_management_portal.interactors\
    .create_update_prefilled_codes_interactor\
    import CreateUpdatePrefilledCodesInteractor


def test_create_update_prefilled_code_given_invalid_question_returns_exception(
        prefilled_codes_dto):

    # Arrange
    question_id = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    interactor = CreateUpdatePrefilledCodesInteractor(
        question_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage
    )
    question_storage.validate_question_id.return_value = False
    presenter.raise_exception_for_invalid_question.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_prefilled_codes(
            question_id=question_id,
            prefilled_codes_dto=prefilled_codes_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    presenter.raise_exception_for_invalid_question.assert_called_once()


def test_create_update_prefilled_code_given_invalid_prefilled_code_returns_exception(
        prefilled_codes_dto):

    # Arrange
    question_id = 1
    prefilled_code_ids = [1]
    db_prefilled_code_ids = [2]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    interactor = CreateUpdatePrefilledCodesInteractor(
        question_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage
    )
    question_storage.validate_question_id.return_value = True
    prefilled_code_storage.get_database_prefilled_code_ids\
        .return_value = db_prefilled_code_ids
    presenter.raise_exception_for_invalid_prefilled_code.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_update_prefilled_codes(
            question_id=question_id,
            prefilled_codes_dto=prefilled_codes_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.get_database_prefilled_code_ids.assert_called_once_with(
        prefilled_code_ids=prefilled_code_ids
    )
    presenter.raise_exception_for_invalid_prefilled_code.assert_called_once()


def test_create_update_prefilled_code_given_different_question_prefilled_code_returns_exception(
        prefilled_codes_dto):

    # Arrange
    question_id = 1
    prefilled_code_ids = [1]
    prefilled_code_question_ids = [1,2]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    interactor = CreateUpdatePrefilledCodesInteractor(
        question_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage
    )
    question_storage.validate_question_id.return_value = True
    prefilled_code_storage.get_database_prefilled_code_ids\
        .return_value = prefilled_code_ids
    prefilled_code_storage.get_prefilled_codes_question_ids\
        .return_value = prefilled_code_question_ids
    presenter.raise_exception_for_different_question.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.create_update_prefilled_codes(
            question_id=question_id,
            prefilled_codes_dto=prefilled_codes_dto
        )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.get_database_prefilled_code_ids.assert_called_once_with(
        prefilled_code_ids=prefilled_code_ids
    )
    prefilled_code_storage.get_prefilled_codes_question_ids.assert_called_once_with(
        prefilled_code_ids=prefilled_code_ids)
    prefilled_code_storage.get_prefilled_codes_question_ids.assert_called_once_with(
        prefilled_code_ids=prefilled_code_ids)
    presenter.raise_exception_for_different_question.assert_called_once()


def test_create_update_prefilled_code_given_valid_details_returns_details(
        prefilled_codes_dto, new_prefilled_codes_dto,
        update_prefilled_codes_dto, prefilled_codes_dto_response):

    # Arrange
    storage_prefilled_codes_dto = [
        PrefilledCodeDto(
            id=1, file_name="prime.py", language_type="PYTHON",
            text_code="text code for python", question_id=1, user_id=1
        ),
        PrefilledCodeDto(
            id=2, file_name="java.py", language_type="JAVA",
            text_code="text code for java", question_id=1, user_id=1
        )
    ]
    question_id = 1
    prefilled_code_ids = [1]
    prefilled_code_question_ids = [1]
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    prefilled_code_storage = create_autospec(PrefilledCodeStorageInterface)
    interactor = CreateUpdatePrefilledCodesInteractor(
        question_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage
    )
    question_storage.validate_question_id.return_value = True
    prefilled_code_storage.get_database_prefilled_code_ids\
        .return_value = prefilled_code_ids
    prefilled_code_storage.get_prefilled_codes_question_ids\
        .return_value = prefilled_code_question_ids
    prefilled_code_storage.get_prefilled_codes_to_question\
        .return_value = storage_prefilled_codes_dto
    presenter.get_response_for_create_update_prefilled_codes\
        .return_value = prefilled_codes_dto_response

    # Act
    interactor_response = interactor.create_update_prefilled_codes(
        question_id=question_id,
        prefilled_codes_dto=prefilled_codes_dto
    )

    # Assert
    question_storage.validate_question_id.assert_called_once_with(
        question_id=question_id
    )
    prefilled_code_storage.get_database_prefilled_code_ids\
        .assert_called_once_with(prefilled_code_ids=prefilled_code_ids)
    prefilled_code_storage.get_prefilled_codes_question_ids\
        .assert_called_once_with(prefilled_code_ids=prefilled_code_ids)
    prefilled_code_storage.get_prefilled_codes_question_ids\
        .assert_called_once_with(prefilled_code_ids=prefilled_code_ids)
    prefilled_code_storage.update_prefilled_codes.assert_called_once_with(
        question_id=question_id,
        prefilled_codes_dto=update_prefilled_codes_dto)
    prefilled_code_storage.create_prefilled_codes.assert_called_once_with(
        prefilled_codes_dto=new_prefilled_codes_dto)
    presenter.get_response_for_create_update_prefilled_codes\
        .assert_called_once_with(
            prefilled_codes_dto=storage_prefilled_codes_dto
        )
