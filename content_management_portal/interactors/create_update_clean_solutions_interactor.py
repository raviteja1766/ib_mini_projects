from typing import List
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import CleanSolutionDto


class CreateUpdateCleanSolutionsInteractor:

    def __init__(self, presenter: PresenterInterface,
                 clean_solution_storage: CleanSolutionStorageInterface,
                 question_storage: QuestionStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.clean_solution_storage = clean_solution_storage

    def create_update_clean_solutions(
            self, question_id: int,
            clean_solutions_dto: List[CleanSolutionDto]):
        self._validations_for_question(question_id=question_id)
        new_clean_solutions_dto, update_clean_solutions_dto =\
            self._get_new_and_update_clean_solutions_dto(clean_solutions_dto)
        if self._is_for_update_clean_solutions_exist(update_clean_solutions_dto):
            self._validations_for_update_clean_solutions_dto(
                question_id, update_clean_solutions_dto)
            self.clean_solution_storage.update_clean_solutions(
                question_id=question_id,
                clean_solutions_dto=update_clean_solutions_dto)
        self.clean_solution_storage.create_clean_solutions(
            clean_solutions_dto=new_clean_solutions_dto
        )
        clean_solutions_dto = self.clean_solution_storage\
            .get_clean_solutions_to_question(question_id=question_id)
        return self.presenter.get_response_for_create_update_clean_solutions(
            clean_solutions_dto=clean_solutions_dto
        )

    def _validations_for_question(self, question_id: int):

        is_invalid_question = not self.question_storage\
            .validate_question_id(question_id=question_id)
        if is_invalid_question:
            self.presenter.raise_exception_for_invalid_question()

    def _validations_for_update_clean_solutions_dto(
            self, question_id: int,
            clean_solutions_dto: List[CleanSolutionDto]):
        clean_solution_ids = self._get_clean_solution_ids(
            clean_solutions_dto=clean_solutions_dto
        )
        db_clean_solution_ids = self.clean_solution_storage\
            .get_database_clean_solution_ids(clean_solution_ids)
        sorted_update_clean_solution_ids = sorted(clean_solution_ids)
        is_invalid_clean_solution = (
            not db_clean_solution_ids == sorted_update_clean_solution_ids
        )
        if is_invalid_clean_solution:
            self.presenter.raise_exception_for_invalid_clean_solution()

        self._validations_for_update_clean_solutions_questions(
            question_id=question_id,
            clean_solution_ids=clean_solution_ids
        )

    @staticmethod
    def _is_for_update_clean_solutions_exist(
            clean_solutions_dto: List[CleanSolutionDto]):

        is_clean_solutions_exists = len(clean_solutions_dto)
        bool_field = False

        if is_clean_solutions_exists:
            bool_field = True

        return bool_field

    def _validations_for_update_clean_solutions_questions(
            self, question_id: int,clean_solution_ids: List[int]):

        clean_solution_question_ids = self.clean_solution_storage\
            .get_clean_solutions_question_ids(clean_solution_ids)
        is_different_question =\
            not clean_solution_question_ids == [question_id]
        if is_different_question:
            self.presenter.raise_exception_for_different_question()

    @staticmethod
    def _get_clean_solution_ids(clean_solutions_dto: List[CleanSolutionDto]):

        return [
            clean_solution_dto.id
            for clean_solution_dto in clean_solutions_dto
        ]

    def _get_new_and_update_clean_solutions_dto(
            self, clean_solutions_dto: List[CleanSolutionDto]):

        new_clean_solutions_dto, update_clean_solutions_dto = [], []
        for clean_solution_dto in clean_solutions_dto:
            if self._check_for_update_clean_solution_dto(clean_solution_dto):
                update_clean_solutions_dto.append(clean_solution_dto)
            else:
                new_clean_solutions_dto.append(clean_solution_dto)
        return new_clean_solutions_dto, update_clean_solutions_dto

    @staticmethod
    def _check_for_update_clean_solution_dto(
            clean_solution_dto: CleanSolutionDto):

        clean_solution_id = clean_solution_dto.id
        is_update_clean_solution = clean_solution_id
        response = False

        if is_update_clean_solution:
            response = True

        return response
