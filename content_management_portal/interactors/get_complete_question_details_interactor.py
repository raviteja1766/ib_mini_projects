from typing import Dict, Any
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin


class GetQuestionCompleteDetailsInteractor(QuestionValidationMixin):

    def __init__(self, presenter: PresenterInterface,
                 question_storage: QuestionStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage

    def get_complete_question_details(
            self, question_id: int) -> Dict[str, Any]:

        self.validate_question_id(question_id=question_id)

        (question_dto, rough_solutions_dto, test_cases_dto, prefilled_codes_dto,
        solution_approach_dto, clean_solutions_dto, hints_dto) = \
            self.question_storage.get_complete_question_details_dto(
                question_id=question_id)
        return self.presenter.get_response_for_complete_question_details(
            question_dto=question_dto,
            rough_solutions_dto=rough_solutions_dto,
            test_cases_dto=test_cases_dto,
            prefilled_codes_dto=prefilled_codes_dto,
            solution_approach_dto=solution_approach_dto,
            clean_solutions_dto=clean_solutions_dto,
            hints_dto=hints_dto
        )
