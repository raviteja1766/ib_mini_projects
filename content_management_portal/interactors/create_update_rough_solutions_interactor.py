from typing import List
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import RoughSolutionDto
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin


class CreateUpdateRoughSolutionsInteractor(QuestionValidationMixin):

    def __init__(self, presenter: PresenterInterface,
                 rough_storage: RoughSolutionStorageInterface,
                 question_storage: QuestionStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.rough_storage = rough_storage

    def create_update_rough_solutions(
            self, question_id: int,
            rough_solutions_dto: List[RoughSolutionDto]):
        self.validate_question_id(question_id=question_id)
        new_rough_solutions_dto, update_rough_solutions_dto =\
            self._get_new_and_update_rough_solutions_dto(rough_solutions_dto)

        if self._is_update_rough_solutions_exist(update_rough_solutions_dto):
            self._validations_for_update_rough_solutions_dto(
                question_id, update_rough_solutions_dto)
            self.rough_storage.update_rough_solutions(
                question_id=question_id,
                rough_solutions_dto=update_rough_solutions_dto)
        self.rough_storage.create_rough_solutions(
            rough_solutions_dto=new_rough_solutions_dto)

        rough_solutions_dto = self.rough_storage\
            .get_rough_solutions_to_question(question_id=question_id)

        return self.presenter.get_response_for_create_update_rough_solutions(
            rough_solutions_dto=rough_solutions_dto)

    @staticmethod
    def _is_update_rough_solutions_exist(
            rough_solutions_dto: List[RoughSolutionDto]):

        is_rough_solutions_exists = len(rough_solutions_dto)
        bool_field = False

        if is_rough_solutions_exists:
            bool_field = True

        return bool_field

    def _validations_for_update_rough_solutions_dto(
            self, question_id: int,
            rough_solutions_dto: List[RoughSolutionDto]):
        rough_solution_ids = self._get_rough_solution_ids(
            rough_solutions_dto=rough_solutions_dto
        )
        db_rough_solution_ids = self.rough_storage\
            .get_database_rough_solution_ids(rough_solution_ids)
        sorted_update_rough_solution_ids = sorted(rough_solution_ids)
        is_invalid_rough_solution = (
            not db_rough_solution_ids == sorted_update_rough_solution_ids
        )
        if is_invalid_rough_solution:
            self.presenter.raise_exception_for_invalid_rough_solution()

        self._validations_for_update_rough_solutions_questions(
            question_id=question_id,
            rough_solution_ids=rough_solution_ids
        )

    def _validations_for_update_rough_solutions_questions(
            self, question_id: int,rough_solution_ids: List[int]):

        rough_solution_question_ids = self.rough_storage\
            .get_rough_solutions_question_ids(rough_solution_ids)
        is_different_question =\
            not rough_solution_question_ids == [question_id]
        if is_different_question:
            self.presenter.raise_exception_for_different_question()

    @staticmethod
    def _get_rough_solution_ids(rough_solutions_dto: List[RoughSolutionDto]):

        return [
            rough_solution_dto.id
            for rough_solution_dto in rough_solutions_dto
        ]

    def _get_new_and_update_rough_solutions_dto(
            self, rough_solutions_dto: List[RoughSolutionDto]):

        new_rough_solutions_dto, update_rough_solutions_dto = [], []
        for rough_solution_dto in rough_solutions_dto:
            if self._check_for_update_rough_solution_dto(rough_solution_dto):
                update_rough_solutions_dto.append(rough_solution_dto)
            else:
                new_rough_solutions_dto.append(rough_solution_dto)
        return new_rough_solutions_dto, update_rough_solutions_dto

    @staticmethod
    def _check_for_update_rough_solution_dto(
            rough_solution_dto: RoughSolutionDto):

        rough_solution_id = rough_solution_dto.id
        is_update_rough_solution = rough_solution_id
        response = False

        if is_update_rough_solution:
            response = True

        return response
