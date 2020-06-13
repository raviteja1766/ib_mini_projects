from abc import ABC
from abc import abstractmethod
from typing import Optional, List, Dict
from content_management_portal.constants.enums import DescriptionType
from content_management_portal.interactors.storages.dtos\
    import RoughSolutionDto


class RoughSolutionStorageInterface(ABC):

    @abstractmethod
    def validate_rough_solution_id(self, rough_solution_id: int) -> bool:
        pass

    @abstractmethod
    def get_question_to_rough_solution(self, rough_solution_id: int) -> int:
        pass

    @abstractmethod
    def delete_rough_solution(self, rough_solution_id: int):
        pass

    @abstractmethod
    def get_rough_solutions_question_ids(
            self, rough_solution_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def create_rough_solutions(
            self, rough_solutions_dto: List[RoughSolutionDto]):
        pass

    @abstractmethod
    def update_rough_solutions(
            self,question_id: int,
            rough_solutions_dto: List[RoughSolutionDto]):
        pass

    @abstractmethod
    def get_rough_solutions_to_question(
            self, question_id: int) -> List[RoughSolutionDto]:
        pass

    @abstractmethod
    def get_database_rough_solution_ids(
            self, rough_solution_ids: List[int]) -> List[int]:
        pass
