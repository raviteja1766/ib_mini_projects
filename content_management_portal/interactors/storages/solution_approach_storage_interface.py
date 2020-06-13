from abc import ABC
from abc import abstractmethod
from content_management_portal.interactors.storages.dtos\
    import SolutionApproachDto


class SolutionApproachStorageInterface(ABC):

    @abstractmethod
    def create_solution_approach(
            self, solution_approach_dto: SolutionApproachDto
            ) -> SolutionApproachDto:
        pass

    @abstractmethod
    def update_solution_approach(
            self, solution_approach_dto: SolutionApproachDto
            ) -> SolutionApproachDto:
        pass

    @abstractmethod
    def validate_solution_approach(self, solution_approach_id: int) -> bool:
        pass

    @abstractmethod
    def get_question_to_solution_approach(
            self, solution_approach_id: int) -> int:
        pass

    @abstractmethod
    def check_if_solution_approach_exists(self, question_id: int) -> bool:
        pass