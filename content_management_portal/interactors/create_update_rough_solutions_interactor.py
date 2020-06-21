from typing import List, Any
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import RoughSolutionDto
from content_management_portal.exceptions.exceptions \
    import InvalidRoughSolution, RoughSolutionsQuestionMisMatch
from content_management_portal.interactors\
    .base_create_update_solutions_interactor\
    import BaseCreateUpdateSolutionsInteractor


class CreateUpdateRoughSolutionsInteractor(
        BaseCreateUpdateSolutionsInteractor):

    def __init__(self, question_id: int, solutions_dto: List[Any],
                 rough_storage: RoughSolutionStorageInterface,
                 question_storage: QuestionStorageInterface):
        super().__init__(question_id, solutions_dto, question_storage)
        self.rough_storage = rough_storage


    def validations_for_update_solution_ids(self, solution_ids: List[int]):

        rough_solution_ids = solution_ids
        db_rough_solution_ids = self.rough_storage\
            .get_database_rough_solution_ids(rough_solution_ids)

        sorted_update_rough_solution_ids = sorted(rough_solution_ids)
        is_invalid_rough_solution = (
            not db_rough_solution_ids == sorted_update_rough_solution_ids
        )
        if is_invalid_rough_solution:
            raise InvalidRoughSolution

        rough_solution_question_ids = self.rough_storage\
            .get_rough_solutions_question_ids(rough_solution_ids)
        is_different_question =\
            not rough_solution_question_ids == [self.question_id]
        if is_different_question:
            raise RoughSolutionsQuestionMisMatch

    def create_solutions_dto(self, solutions_dto: List[RoughSolutionDto]):

        self.rough_storage\
            .create_rough_solutions(rough_solutions_dto=solutions_dto)

    def update_solutions_dto(self, solutions_dto: List[RoughSolutionDto]):

        self.rough_storage.update_rough_solutions(
            question_id=self.question_id,
            rough_solutions_dto=solutions_dto
        )

    def get_solutions_of_question(self):

        return self.rough_storage.get_rough_solutions_to_question(
            question_id=self.question_id
        )
