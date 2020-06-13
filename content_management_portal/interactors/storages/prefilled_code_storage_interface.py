from abc import ABC
from abc import abstractmethod
from typing import Optional, List
from content_management_portal.interactors.storages.dtos\
    import PrefilledCodeDto


class PrefilledCodeStorageInterface(ABC):

    @abstractmethod
    def update_prefilled_codes(
            self, question_id: int,
            prefilled_codes_dto: List[PrefilledCodeDto]):
        pass

    @abstractmethod
    def create_prefilled_codes(
            self, prefilled_codes_dto: List[PrefilledCodeDto]):
        pass

    @abstractmethod
    def get_prefilled_codes_to_question(
            self, question_id: int) -> List[PrefilledCodeDto]:
        pass

    @abstractmethod
    def get_database_prefilled_code_ids(
            self, prefilled_code_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_prefilled_codes_question_ids(
            self, prefilled_code_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def validate_prefilled_code(self, prefilled_code_id: int) -> bool:
        pass

    @abstractmethod
    def delete_prefilled_code(self, prefilled_code_id: int):
        pass

    @abstractmethod
    def get_question_to_prefilled_code(self, prefilled_code_id: int) -> int:
        pass
