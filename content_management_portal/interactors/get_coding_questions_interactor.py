from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.constants.constants\
    import check_for_none_values_of_offset_and_limit,\
    validate_offset, validate_limit
from content_management_portal.interactors.storages.dtos\
    import CodingQuestionDto


class GetCodingQuestionsInteractors:

    def __init__(self, presenter: PresenterInterface,
                 question_storage: QuestionStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage

    def get_coding_questions_details(self, offset: int, limit: int):

        offset, limit = check_for_none_values_of_offset_and_limit(
            offset=offset, limit=limit)
        questions_count =\
            self.question_storage.get_total_questions_count()
        self._validations_for_offset_and_limit(offset, limit, questions_count)

        coding_questions_dto = self.question_storage\
            .get_coding_questions_details_dto(offset=offset, limit=limit)
        checked_coding_questions_dto = [
            self._check_and_get_coding_question_dto(question_dto)
            for question_dto in coding_questions_dto
        ]
        return self.presenter.get_response_for_get_coding_questions_details(
            offset=offset, limit=limit,
            questions_count=questions_count,
            coding_questions_dto=checked_coding_questions_dto
        )

    @staticmethod
    def _check_and_get_coding_question_dto(question_dto):

        zero = 0
        return CodingQuestionDto(
            question_id=question_dto.question_id,
            short_text=question_dto.short_text,
            rough_solutions=question_dto.rough_solutions != zero,
            test_cases=question_dto.test_cases != zero,
            prefilled_code=question_dto.prefilled_code != zero,
            solution_approach=question_dto.solution_approach != zero,
            clean_solution=question_dto.clean_solution != zero
        )

    def _validations_for_offset_and_limit(
            self, offset, limit, questions_count):

        is_invalid_offset = not validate_offset(offset, questions_count)
        if is_invalid_offset:
            self.presenter.raise_exception_for_offset_exception()
        is_invalid_limit = not validate_limit(limit)
        if is_invalid_limit:
            self.presenter.raise_exception_for_limit_exception()
