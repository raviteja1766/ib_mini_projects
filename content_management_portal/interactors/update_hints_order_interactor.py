from typing import List, Dict
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import HintSwapDto

class UpdateHintsOrderInteractor:

    def __init__(
            self, presenter: PresenterInterface,
            question_storage: QuestionStorageInterface,
            hint_storage: HintStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.hint_storage = hint_storage

    def update_hints_order(
            self, question_id: int, hints_dto: List[HintSwapDto]):

        self._validations_for_question(question_id=question_id)
        self._validations_for_hints_dto(question_id, hints_dto)
        hints_dto = self.swap_hints_dto_order_id(hints_dto)
        self.hint_storage.update_hints_order(hints_dto)

    def _validations_for_question(self, question_id: int):

        is_invalid_question = not self.question_storage\
            .validate_question_id(question_id=question_id)
        if is_invalid_question:
            self.presenter.raise_exception_for_invalid_question()

    def _validations_for_hints_dto(
            self, question_id: int, hints_dto: List[HintSwapDto]):

        hint_ids = [
            hint_dto.id for hint_dto in hints_dto
        ]
        db_hint_ids = self.hint_storage\
            .get_database_hint_ids(hint_ids)
        sorted_hint_ids = sorted(hint_ids)
        is_invalid_hint = (
            not db_hint_ids == sorted_hint_ids
        )
        if is_invalid_hint:
            self.presenter.raise_exception_for_invalid_hint()

        self._validations_for_hints_questions(
            question_id=question_id,
            hint_ids=hint_ids
        )

    def _validations_for_hints_questions(
            self, question_id: int,hint_ids: List[int]):

        hint_question_ids = self.hint_storage\
            .get_hints_question_ids(hint_ids)
        is_different_question =\
            not hint_question_ids == [question_id]
        if is_different_question:
            self.presenter.raise_exception_for_different_question()

    def swap_hints_dto_order_id(
            self, hints_dto: List[HintSwapDto]):

        first_hint_dto = hints_dto[0]
        second_hint_dto = hints_dto[-1]
        temp_order_id = first_hint_dto.order_id
        first_hint_dto.order_id = second_hint_dto.order_id
        second_hint_dto.order_id =temp_order_id

        hints_dto = [first_hint_dto, second_hint_dto]
        return hints_dto