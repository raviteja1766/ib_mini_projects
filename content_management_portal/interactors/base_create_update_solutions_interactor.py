from typing import List, Any
from abc import abstractmethod
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin, DuplicateIdsValidationMixin
from content_management_portal.interactors.storages.dtos \
    import SolutionDto
from content_management_portal.exceptions.exceptions import (
    InvalidQuestionId, InvalidRoughSolution, RoughSolutionsQuestionMisMatch
)


class DuplicateIds(Exception):
    pass


class BaseCreateUpdateSolutionsInteractor(
        QuestionValidationMixin, DuplicateIdsValidationMixin):

    def __init__(self, question_id: int,
                 solutions_dto: List[Any],
                 question_storage: QuestionStorageInterface):
        self.question_id = question_id
        self.solutions_dto = solutions_dto
        self.question_storage = question_storage

    def base_create_update_solutions_wrapper(self, presenter: PresenterInterface):

        try:
            storage_solutions_dto = self.base_create_update_solutions()
            return presenter\
                .get_response_for_base_create_update_solutions_wrapper(
                    solutions_dto=storage_solutions_dto)
        except InvalidQuestionId:
            presenter.raise_exception_for_invalid_question()
        except DuplicateIds:
            presenter.raise_exception_for_duplicate_ids()
        except InvalidRoughSolution:
            presenter.raise_exception_for_invalid_rough_solution()
        except RoughSolutionsQuestionMisMatch:
            presenter.raise_exception_for_different_question()


    def base_create_update_solutions(self):

        self.validate_question(question_id=self.question_id)
        new_solutions_dto, update_solutions_dto = \
            self._get_new_and_update_solutions_dto(
                solutions_dto=self.solutions_dto
            )

        if self._is_update_solutions_exist(update_solutions_dto):
            self._update_solutions_dto(solutions_dto=update_solutions_dto)

        if self._is_new_solutions_exist(new_solutions_dto):
            self.create_solutions_dto(solutions_dto=new_solutions_dto)

        return self.get_solutions_of_question()

    def _update_solutions_dto(self, solutions_dto: List[SolutionDto]):
        solution_ids = self._get_solution_ids(solutions_dto=solutions_dto)
        if self.is_duplicate_ids_present(list_of_ids=solution_ids):
            raise DuplicateIds
        self.validations_for_update_solution_ids(solution_ids=solution_ids)
        self.update_solutions_dto(solutions_dto=solutions_dto)

    @abstractmethod
    def create_solutions_dto(self, solutions_dto: List[SolutionDto]):
        pass

    @abstractmethod
    def update_solutions_dto(self, solutions_dto: List[SolutionDto]):
        pass

    @abstractmethod
    def get_solutions_of_question(self):
        pass

    @abstractmethod
    def validations_for_update_solution_ids(self, solution_ids: List[int]):
        pass


    @staticmethod
    def _get_solution_ids(solutions_dto: List[SolutionDto]):

        return [
            solution_dto.id
            for solution_dto in solutions_dto
        ]


    def _is_update_solutions_exist(self, solutions_dto: List[SolutionDto]):

        return self._is_solutions_exist(solutions_dto)

    def _is_new_solutions_exist(self, solutions_dto: List[SolutionDto]):

        return self._is_solutions_exist(solutions_dto)

    @staticmethod
    def _is_solutions_exist(solutions_dto: List[Any]):
        is_solutions_exists = len(solutions_dto)
        bool_field = False

        if is_solutions_exists:
            bool_field = True

        return bool_field

    def _get_new_and_update_solutions_dto(
            self, solutions_dto: List[SolutionDto]):

        new_solutions_dto, update_solutions_dto = [], []
        for solution_dto in solutions_dto:
            if self._check_for_update_solution_dto(solution_dto):
                update_solutions_dto.append(solution_dto)
            else:
                new_solutions_dto.append(solution_dto)
        return new_solutions_dto, update_solutions_dto

    @staticmethod
    def _check_for_update_solution_dto(solution_dto: SolutionDto):

        solution_id = solution_dto.id
        is_update_solution = solution_id
        bool_field = False

        if is_update_solution:
            bool_field = True

        return bool_field
