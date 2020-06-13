from typing import List
from content_management_portal.interactors.storages\
    .rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.models import RoughSolution, Question
from content_management_portal.interactors.storages.dtos\
    import RoughSolutionDto


class RoughSolutionStorageImplementation(RoughSolutionStorageInterface):

    def validate_rough_solution_id(self, rough_solution_id: int) -> bool:

        return RoughSolution.objects.filter(id=rough_solution_id).exists()

    def get_question_to_rough_solution(self, rough_solution_id: int) -> int:

        rough_solution_obj = RoughSolution.objects.get(id=rough_solution_id)
        return rough_solution_obj.question_id

    def delete_rough_solution(self, rough_solution_id: int):

        RoughSolution.objects.filter(id=rough_solution_id).delete()

    def get_rough_solutions_question_ids(
            self, rough_solution_ids: List[int]) -> List[int]:

        question_ids = Question.objects\
            .filter(roughsolution__id__in=rough_solution_ids)\
            .values_list('id', flat=True)
        return list(set(question_ids))

    def create_rough_solutions(
            self, rough_solutions_dto: List[RoughSolutionDto]):

        RoughSolution.objects.bulk_create([
            RoughSolution(
                file_name=rough_solution.file_name,
                language=rough_solution.language_type,
                code=rough_solution.text_code,
                question_id=rough_solution.question_id,
                user_id=rough_solution.user_id
            )
            for rough_solution in rough_solutions_dto
        ])

    def update_rough_solutions(
            self,question_id: int,
            rough_solutions_dto: List[RoughSolutionDto]):

        rough_solutions_dict = {}
        for rough_solution in rough_solutions_dto:
            rough_solutions_dict[rough_solution.id] = rough_solution

        rough_solution_objs = RoughSolution.objects\
            .filter(question_id=question_id)

        self._bulk_update_rough_solutions(
            rough_solution_objs, rough_solutions_dict)

    @staticmethod
    def _bulk_update_rough_solutions(
            rough_solution_objs, rough_solutions_dict):

        for rough_solution_obj in rough_solution_objs:
            rough_solution_dto = rough_solutions_dict[rough_solution_obj.id]
            rough_solution_obj.file_name = rough_solution_dto.file_name
            rough_solution_obj.language = rough_solution_dto.language_type
            rough_solution_obj.code = rough_solution_dto.text_code

        RoughSolution.objects.bulk_update(
            rough_solution_objs, ['file_name', 'language', 'code'])

    def get_rough_solutions_to_question(self, question_id: int):

        rough_solution_objs = RoughSolution.objects\
            .filter(question_id=question_id)
        return [
            RoughSolutionDto(
                id=rough_solution_obj.id,
                file_name=rough_solution_obj.file_name,
                language_type=rough_solution_obj.language,
                text_code=rough_solution_obj.code,
                question_id=rough_solution_obj.question_id,
                user_id=rough_solution_obj.user_id
            )
            for rough_solution_obj in rough_solution_objs
        ]

    def get_database_rough_solution_ids(
            self, rough_solution_ids: List[int]):

        rough_solution_ids = RoughSolution.objects\
                .filter(id__in=rough_solution_ids)\
                .values_list('id', flat=True)
        return list(rough_solution_ids)
