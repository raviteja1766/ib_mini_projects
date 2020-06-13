from abc import ABC
from abc import abstractmethod
from typing import List, Tuple, Any
from content_management_portal.constants.enums import DescriptionType
from content_management_portal.interactors.storages.dtos import (
    QuestionDto, CodingQuestionDto, RoughSolutionDto
)


class QuestionStorageInterface(ABC):

    @abstractmethod
    def validate_question_id(self, question_id: int) -> bool:
        pass

    @abstractmethod
    def create_question(self, question_dto: QuestionDto) -> QuestionDto:
        pass

    @abstractmethod
    def update_question(self, question_dto: QuestionDto) -> QuestionDto:
        pass

    @abstractmethod
    def get_user_to_question(self, question_id: int) -> int:
        pass

    @abstractmethod
    def get_coding_questions_details_dto(
            self, offset: int, limit: int) -> List[CodingQuestionDto]:
        pass

    @abstractmethod
    def get_complete_question_details_dto(
            self, question_id: int) -> Tuple[Any]:
        pass

    @abstractmethod
    def get_total_questions_count(self) -> int:
        pass