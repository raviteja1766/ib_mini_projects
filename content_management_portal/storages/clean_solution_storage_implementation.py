from typing import List
from content_management_portal.interactors.storages.dtos\
    import CleanSolutionDto
from content_management_portal.interactors.storages\
    .clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors\
    .create_update_clean_solutions_interactor\
    import CreateUpdateCleanSolutionsInteractor
from content_management_portal.models import CleanSolution, Question


class CleanSolutionStorageImplementation(CleanSolutionStorageInterface):

    def update_clean_solutions(
            self,question_id: int,
            clean_solutions_dto: List[CleanSolutionDto]):
        clean_solutions_dto_dict = {}

        for clean_solution_dto in clean_solutions_dto:
            clean_solutions_dto_dict[clean_solution_dto.id] =\
                clean_solution_dto

        clean_solution_objs = CleanSolution.objects\
            .filter(question_id=question_id)

        for clean_solution_obj in clean_solution_objs:
            clean_solution_dto =\
                clean_solutions_dto_dict[clean_solution_obj.id]
            self._update_single_clean_solution(
                clean_solution_obj, clean_solution_dto)

        CleanSolution.objects.bulk_update(
            clean_solution_objs, ["file_name", "language", "code"]
        )

    @staticmethod
    def _update_single_clean_solution(clean_solution_obj, clean_solution_dto):

        clean_solution_obj.file_name=clean_solution_dto.file_name
        clean_solution_obj.language=clean_solution_dto.language_type
        clean_solution_obj.code=clean_solution_dto.text_code

    def create_clean_solutions(
            self, clean_solutions_dto: List[CleanSolutionDto]):

        CleanSolution.objects.bulk_create([
            CleanSolution(
                file_name=clean_solution_dto.file_name,
                language=clean_solution_dto.language_type,
                code=clean_solution_dto.text_code,
                question_id=clean_solution_dto.question_id,
                user_id=clean_solution_dto.user_id
            ) for clean_solution_dto in clean_solutions_dto
        ])


    def get_clean_solutions_to_question(
            self, question_id: int) -> List[CleanSolutionDto]:

        clean_solution_objs = CleanSolution.objects\
            .filter(question_id=question_id)
        return [
            CleanSolutionDto(
                id=clean_solution_obj.id,
                file_name=clean_solution_obj.file_name,
                language_type=clean_solution_obj.language,
                text_code=clean_solution_obj.code,
                question_id=clean_solution_obj.question_id,
                user_id=clean_solution_obj.user_id
            ) for clean_solution_obj in clean_solution_objs
        ]

    def get_database_clean_solution_ids(
            self, clean_solution_ids: List[int]) -> List[int]:

        clean_solution_ids = CleanSolution.objects\
            .filter(id__in=clean_solution_ids)\
            .values_list('id', flat=True)

        return list(clean_solution_ids)

    def get_clean_solutions_question_ids(
            self, clean_solution_ids: List[int]) -> List[int]:

        clean_solutions_question_ids = Question.objects\
            .filter(cleansolution__id__in=clean_solution_ids)\
            .values_list('id', flat=True)

        return list(set(clean_solutions_question_ids))

    def validate_clean_solution(self, clean_solution_id: int) -> bool:

        return CleanSolution.objects.filter(id=clean_solution_id).exists()

    def delete_clean_solution(self, clean_solution_id: int):

        CleanSolution.objects.filter(id=clean_solution_id).delete()

    def get_question_to_clean_solution(self, clean_solution_id: int) -> int:

        clean_solution_obj = CleanSolution.objects.get(id=clean_solution_id)
        question_id = clean_solution_obj.question_id
        return question_id
