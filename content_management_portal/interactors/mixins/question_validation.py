
from typing import List


class QuestionValidationMixin:

    def validate_question_id(self, question_id: int):
        is_invalid_question = not self.question_storage\
            .validate_question_id(question_id=question_id)
        if is_invalid_question:
            self.presenter.raise_exception_for_invalid_question()


class DuplicateIdsValidationMixin:

    def is_duplicate_ids_present(self, list_of_ids: List[int]) -> bool:

        unique_ids_length = len(set(list_of_ids))
        list_of_ids_lenght = len(list_of_ids)
        bool_field = False
        is_not_same_length = not unique_ids_length == list_of_ids_lenght
        if is_not_same_length:
            bool_field = True

        return bool_field