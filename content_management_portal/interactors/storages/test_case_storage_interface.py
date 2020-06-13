from abc import ABC
from abc import abstractmethod
from typing import Optional, List
from content_management_portal.interactors.storages.dtos\
    import TestCaseDto, TestCaseSwapDto


class TestCaseStorageInterface(ABC):

    @abstractmethod
    def create_test_case(self, test_case_dto: TestCaseDto) -> TestCaseDto:
        pass

    @abstractmethod
    def update_test_case(self, test_case_dto: TestCaseDto) -> TestCaseDto:
        pass

    @abstractmethod
    def validate_test_case(self, test_case_id: int) -> bool:
        pass

    @abstractmethod
    def get_question_to_test_case(
            self, test_case_id: int) -> int:
        pass

    @abstractmethod
    def delete_test_case_and_get_test_case_order(
            self, test_case_id: int) -> int:
        pass

    @abstractmethod
    def update_questions_next_test_cases_order(
            self, question_id: int, order_id: int):
        pass

    @abstractmethod
    def update_test_cases_order(self, test_cases_dto: List[TestCaseSwapDto]):
        pass

    @abstractmethod
    def get_database_test_case_ids(
            self, test_case_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_test_cases_question_ids(
            self, test_case_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_max_test_case_order_of_question(
            self, question_id: int) -> Optional[int]:
        pass
