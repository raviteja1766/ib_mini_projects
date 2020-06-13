from typing import List, Dict
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import HintDto

class CreateUpdateHintInteractor:

    def __init__(
            self, presenter: PresenterInterface,
            question_storage: QuestionStorageInterface,
            hint_storage: HintStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.hint_storage = hint_storage

    def create_update_hint(self, hint_dto: HintDto):

        question_id = hint_dto.question_id
        self._validations_for_question(question_id=question_id)
        is_update_hint = not hint_dto.id is None
        if is_update_hint:
            self._validations_for_hint(hint_dto)
            hint_dto = self.hint_storage.update_hint(hint_dto=hint_dto)
        else:
            hint_dto = self._update_hint_dto_order_and_create_hint(hint_dto)
        return self.presenter.get_response_for_create_update_hint(
            hint_dto=hint_dto
        )

    def _update_hint_dto_order_and_create_hint(self, hint_dto: HintDto):

        question_id = hint_dto.question_id
        max_order_id = self.hint_storage\
            .get_max_hint_order_of_question(question_id=question_id)
        is_zero_hints = max_order_id is None
        if is_zero_hints:
            max_order_id = 0
        hint_dto.order_id = max_order_id + 1
        return self.hint_storage.create_hint(hint_dto=hint_dto)

    def _validations_for_hint(self, hint_dto: HintDto):

        is_invalid_hint = not self.hint_storage\
            .validate_hint(hint_id=hint_dto.id)
        if is_invalid_hint:
            self.presenter.raise_exception_for_invalid_hint()
        hint_question_id = self.hint_storage\
            .get_question_to_hint(hint_id=hint_dto.id)
        question_id = hint_dto.question_id
        is_different_question = not hint_question_id == question_id
        if is_different_question:
            self.presenter.raise_exception_for_different_question()

    def _validations_for_question(self, question_id: int):

        is_invalid_question = not self.question_storage\
            .validate_question_id(question_id=question_id)
        if is_invalid_question:
            self.presenter.raise_exception_for_invalid_question()
