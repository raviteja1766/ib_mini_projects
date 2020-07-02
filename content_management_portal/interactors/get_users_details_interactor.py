from typing import List
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface

from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.exceptions.exceptions import (
    DuplicateQuestionIds, InvalidQuestionId,
    DuplicateCMPUserIds, InvalidCMPUserIds
)
from content_management_portal.interactors.mixins.question_validation \
    import DuplicateIdsValidationMixin
from content_management_portal.adapters.service_adapter \
    import get_service_adapter


class GetQuestionsUserDetailsInteractor(DuplicateIdsValidationMixin):

    def __init__(self, question_ids: List[int],
                 question_storage: QuestionStorageInterface):
        self.question_storage = question_storage
        self.question_ids = question_ids

    def get_questions_user_details_wrapper(self, presenter: PresenterInterface):

        try:
            user_dtos = self._get_questions_user_details(
                question_ids=self.question_ids)
            return presenter.get_questions_user_details_response(
                user_dtos=user_dtos)
        except DuplicateQuestionIds:
            presenter.raise_exception_for_duplicate_ids()
        except InvalidQuestionId:
            presenter.raise_exception_for_invalid_question()
        except DuplicateCMPUserIds:
            presenter.raise_exception_for_duplicate_ids()
        except InvalidCMPUserIds:
            presenter.raise_exception_for_invalid_user_ids()


    def _get_questions_user_details(self, question_ids: List[int]):


        if self.is_duplicate_ids_present(list_of_ids=question_ids):
            raise DuplicateQuestionIds
        self._validate_question_ids(question_ids=question_ids)

        user_ids = self.question_storage.get_user_ids_of_questions(
            question_ids=question_ids
        )
        service_adapter = get_service_adapter()
        user_dtos = \
            service_adapter.auth_service.get_user_dtos(user_ids=user_ids)
        return user_dtos

    def _validate_question_ids(self, question_ids: List[int]):

        db_question_ids = self.question_storage.get_valid_question_ids(
            question_ids=question_ids
        )

        is_invalid_question_ids = not len(db_question_ids) == len(question_ids)
        if is_invalid_question_ids:
            raise InvalidQuestionId
