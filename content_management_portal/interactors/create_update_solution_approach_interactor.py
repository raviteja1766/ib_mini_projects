from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .solution_approach_storage_interface \
    import SolutionApproachStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import SolutionApproachDto

class CreateUpdateSolutionApproachInteractor:

    def __init__(
            self, presenter: PresenterInterface,
            question_storage: QuestionStorageInterface,
            solution_approach_storage: SolutionApproachStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.solution_approach_storage = solution_approach_storage

    def create_update_solution_approach(
            self, solution_approach_dto: SolutionApproachDto):

        question_id = solution_approach_dto.question_id
        self._validations_for_question(question_id=question_id)
        is_update_solution_approach = not solution_approach_dto.id is None
        if is_update_solution_approach:
            self._validations_for_solution_approach(solution_approach_dto)
            solution_approach_dto = self.solution_approach_storage\
                .update_solution_approach(
                    solution_approach_dto=solution_approach_dto)
        else:
            self._validate_if_solution_approach_presence(question_id)
            solution_approach_dto = self.solution_approach_storage\
                .create_solution_approach(
                    solution_approach_dto=solution_approach_dto)
        return self.presenter\
            .get_response_for_create_update_solution_approach(
                solution_approach_dto=solution_approach_dto
            )

    def _validations_for_solution_approach(
            self, solution_approach_dto: SolutionApproachDto):

        is_invalid_solution_approach = not self.solution_approach_storage\
            .validate_solution_approach(
                solution_approach_id=solution_approach_dto.id)
        if is_invalid_solution_approach:
            self.presenter.raise_exception_for_invalid_solution_approach()
        solution_approach_question_id = self.solution_approach_storage\
            .get_question_to_solution_approach(
                solution_approach_id=solution_approach_dto.id)
        question_id = solution_approach_dto.question_id
        is_different_question = \
            not solution_approach_question_id == question_id
        if is_different_question:
            self.presenter.raise_exception_for_different_question()

    def _validations_for_question(self, question_id: int):

        is_invalid_question = not self.question_storage\
            .validate_question_id(question_id=question_id)
        if is_invalid_question:
            self.presenter.raise_exception_for_invalid_question()

    def _validate_if_solution_approach_presence(self, question_id: int):
        
        is_solution_approach_already_present =\
            self.solution_approach_storage\
            .check_if_solution_approach_exists(question_id)
        if is_solution_approach_already_present:
            self.presenter.raise_exception_for_solution_approach_exists()
