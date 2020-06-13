from abc import ABC
from abc import abstractmethod
from typing import Optional, List
from content_management_portal.interactors.storages.dtos\
    import HintDto, HintSwapDto


class HintStorageInterface(ABC):

    @abstractmethod
    def create_hint(self, hint_dto: HintDto) -> HintDto:
        pass

    @abstractmethod
    def update_hint(self, hint_dto: HintDto) -> HintDto:
        pass

    @abstractmethod
    def validate_hint(self, hint_id: int) -> bool:
        pass

    @abstractmethod
    def get_question_to_hint(self, hint_id: int) -> int:
        pass

    @abstractmethod
    def delete_hint_and_get_hint_order(self, hint_id: int) -> int:
        pass

    @abstractmethod
    def update_hints_order(self, hints_dto: List[HintSwapDto]):
        pass

    @abstractmethod
    def get_database_hint_ids(self, hint_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_hints_question_ids(self, hint_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_max_hint_order_of_question(
            self, question_id: int) -> Optional[int]:
        pass

    @abstractmethod
    def update_questions_next_hints_order(self, question_id: int,
                                          order_id: int):
        pass
