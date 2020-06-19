from abc import ABC
from abc import abstractmethod
from typing import Optional, List, Dict
from form_master.interactors.storages.dtos import *


class StorageInterface(ABC):

    @abstractmethod
    def get_form_status_dto(self, form_id: int) -> FormStatusDto:
        pass

    @abstractmethod
    def validate_question_id_with_form(self, question_id: int, form_id: int):
        pass

    @abstractmethod
    def get_option_ids_for_question(self, question_id: int) -> List[int]:
        pass

    @abstractmethod
    def create_user_mcq_response(
            self, user_response_dto: UserResponseDTO) -> int:
        pass

    @abstractmethod
    def create_user_text_response(
            self, user_response_dto: UserTextResponseDTO) -> int:
        pass
