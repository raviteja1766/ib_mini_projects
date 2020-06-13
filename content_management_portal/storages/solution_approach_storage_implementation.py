from typing import Optional, List
from django.db.models import Max
from content_management_portal.interactors.storages.dtos\
    import SolutionApproachDto
from content_management_portal.interactors.storages\
    .solution_approach_storage_interface\
    import SolutionApproachStorageInterface
from content_management_portal.models import SolutionApproach, Question


class SolutionApproachStorageImplementation(SolutionApproachStorageInterface):

    def create_solution_approach(
            self, solution_approach_dto: SolutionApproachDto
            ) -> SolutionApproachDto:

        solution_approach_obj = SolutionApproach.objects.create(
            title = solution_approach_dto.title,
            description_content_type = \
                solution_approach_dto.description_content_type,
            description_content = \
                solution_approach_dto.description_content,
            complexity_content = \
                solution_approach_dto.complexity_content,
            complexity_content_type = \
                solution_approach_dto.complexity_content_type,
            question_id=solution_approach_dto.question_id,
            user_id=solution_approach_dto.user_id
        )
        solution_approach_dto.id = solution_approach_obj.id

        return solution_approach_dto

    def update_solution_approach(
            self, solution_approach_dto: SolutionApproachDto
            ) -> SolutionApproachDto:

        solution_approach_id = solution_approach_dto.id
        solution_approach_obj = SolutionApproach.objects\
            .get(id=solution_approach_id)
        solution_approach_obj.title = solution_approach_dto.title
        solution_approach_obj.description_content_type = \
            solution_approach_dto.description_content_type
        solution_approach_obj.description_content = \
            solution_approach_dto.description_content
        solution_approach_obj.complexity_content = \
            solution_approach_dto.complexity_content
        solution_approach_obj.complexity_content_type = \
            solution_approach_dto.complexity_content_type
        solution_approach_obj.save()

        return solution_approach_dto

    def validate_solution_approach(self, solution_approach_id: int) -> bool:

        return SolutionApproach.objects\
            .filter(id=solution_approach_id).exists()

    def get_question_to_solution_approach(
            self, solution_approach_id: int) -> int:

        solution_approach_obj = SolutionApproach.objects\
            .get(id=solution_approach_id)

        return solution_approach_obj.question_id
    
    def check_if_solution_approach_exists(self, question_id: int):

        return SolutionApproach.objects\
            .filter(question_id=question_id).exists()
