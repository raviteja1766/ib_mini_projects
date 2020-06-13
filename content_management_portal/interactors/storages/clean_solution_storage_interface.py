from abc import ABC
from abc import abstractmethod
from typing import Optional, List, Dict
from content_management_portal.interactors.storages.dtos\
    import CleanSolutionDto


class CleanSolutionStorageInterface(ABC):

    @abstractmethod
    def update_clean_solutions(
            self,question_id: int,
            clean_solutions_dto: List[CleanSolutionDto]):
        pass

    @abstractmethod
    def create_clean_solutions(
            self, clean_solutions_dto: List[CleanSolutionDto]):
        pass

    @abstractmethod
    def get_clean_solutions_to_question(
            self, question_id: int) -> List[CleanSolutionDto]:
        pass

    @abstractmethod
    def get_database_clean_solution_ids(
            self, clean_solution_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_clean_solutions_question_ids(
            self, clean_solution_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def validate_clean_solution(self, clean_solution_id: int) -> bool:
        pass

    @abstractmethod
    def delete_clean_solution(self, clean_solution_id: int):
        pass

    @abstractmethod
    def get_question_to_clean_solution(self, clean_solution_id: int) -> int:
        pass
