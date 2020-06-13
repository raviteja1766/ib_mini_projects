import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import BadRequest
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.get_coding_questions_interactor\
    import GetCodingQuestionsInteractors


def test_get_coding_questions_details_returns_questions_details(
        coding_questions_dto, coding_questions_complete_details):

    # Arrange
    offset = 0
    limit = 1
    questions_count = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = GetCodingQuestionsInteractors(
        presenter=presenter, question_storage=question_storage
    )
    question_storage.get_coding_questions_details_dto.return_value =\
        coding_questions_dto
    question_storage.get_total_questions_count.return_value = questions_count
    presenter.get_response_for_get_coding_questions_details.return_value =\
        coding_questions_complete_details

    # Act
    interactor_response = interactor.get_coding_questions_details(
        offset=offset, limit=limit
    )

    # Assert
    question_storage.get_coding_questions_details_dto.assert_called_once_with(
        offset=offset, limit=limit)
    presenter.get_response_for_get_coding_questions_details\
        .assert_called_once_with(
            offset=offset, limit=limit,
            questions_count=questions_count,
            coding_questions_dto=coding_questions_dto
        )

@pytest.mark.parametrize('offset',[0, -1])
def test_get_coding_questions_details_having_negative_offset_returns_exception(
        offset):

    # Arrange
    limit = 1
    questions_count = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = GetCodingQuestionsInteractors(
        presenter=presenter, question_storage=question_storage
    )
    question_storage.get_total_questions_count.return_value = questions_count
    presenter.raise_exception_for_offset_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor_response = interactor.get_coding_questions_details(
            offset=offset, limit=limit
        )

    # Assert
    presenter.raise_exception_for_offset_exception.assert_called_once()


def test_get_coding_questions_details_offset_morethan_questions_count_returns_exception(
        ):

    # Arrange
    offset = 5
    limit = 1
    questions_count = 1
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = GetCodingQuestionsInteractors(
        presenter=presenter, question_storage=question_storage
    )
    question_storage.get_total_questions_count.return_value = questions_count
    presenter.raise_exception_for_offset_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor_response = interactor.get_coding_questions_details(
            offset=offset, limit=limit
        )

    # Assert
    presenter.raise_exception_for_offset_exception.assert_called_once()

@pytest.mark.parametrize('limit',[0, -1])
def test_get_coding_questions_details_when_limit_less_than_or_equals_zero_returns_exception(
        limit):

    # Arrange
    offset = 4
    questions_count = 6
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = GetCodingQuestionsInteractors(
        presenter=presenter, question_storage=question_storage
    )
    question_storage.get_total_questions_count.return_value = questions_count
    presenter.raise_exception_for_limit_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor_response = interactor.get_coding_questions_details(
            offset=offset, limit=limit
        )

    # Assert
    presenter.raise_exception_for_limit_exception.assert_called_once()


def test_get_coding_questions_details_limit_number_greater_than_fixed_limit_returns_exception(
        ):

    # Arrange
    offset = 4
    limit = 13
    questions_count = 6
    presenter = create_autospec(PresenterInterface)
    question_storage = create_autospec(QuestionStorageInterface)
    interactor = GetCodingQuestionsInteractors(
        presenter=presenter, question_storage=question_storage
    )
    question_storage.get_total_questions_count.return_value = questions_count
    presenter.raise_exception_for_limit_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor_response = interactor.get_coding_questions_details(
            offset=offset, limit=limit
        )

    # Assert
    presenter.raise_exception_for_limit_exception.assert_called_once()