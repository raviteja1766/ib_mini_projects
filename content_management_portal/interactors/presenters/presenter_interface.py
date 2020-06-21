from abc import ABC
from abc import abstractmethod
from typing import List, Any
from common.dtos import UserAuthTokensDTO
from content_management_portal.interactors.storages.dtos\
    import (
        QuestionDto, TestCaseDto, RoughSolutionDto,
        PrefilledCodeDto, CleanSolutionDto,
        SolutionApproachDto, HintDto, CodingQuestionDto
    )

class PresenterInterface(ABC):

    @abstractmethod
    def get_response_for_login_user(
            self, user_auth_token_dto: UserAuthTokensDTO):
        pass

    @abstractmethod
    def raise_exception_for_invalid_question(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def get_response_for_question_dto(self, question_dto: QuestionDto):
        pass

    @abstractmethod
    def raise_exception_for_rough_solution_not_in_question(self):
        pass

    @abstractmethod
    def raise_exception_for_user_cannot_delete_question(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_rough_solution(self):
        pass

    @abstractmethod
    def get_response_for_create_update_rough_solutions(
            self, rough_solutions_dto: List[RoughSolutionDto]):
        pass

    @abstractmethod
    def get_response_for_base_create_update_solutions_wrapper(
            self, solutions_dto: List[Any]):
        pass

    @abstractmethod
    def raise_exception_for_user_cannot_update_question(self):
        pass

    @abstractmethod
    def raise_exception_for_different_question(self):
        pass

    @abstractmethod
    def get_response_for_get_coding_questions_details(
            self,offset: int, limit: int, questions_count:int,
            coding_questions_dto: List[CodingQuestionDto]):
        pass

    @abstractmethod
    def get_response_for_complete_question_details(
            self, question_dto: QuestionDto,
            rough_solutions_dto: List[RoughSolutionDto],
            test_cases_dto: List[TestCaseDto],
            prefilled_codes_dto: List[PrefilledCodeDto],
            solution_approach_dto: SolutionApproachDto,
            clean_solutions_dto: List[CleanSolutionDto],
            hints_dto: List[HintDto]
            ):
        pass

    @abstractmethod
    def raise_exception_for_invalid_test_case(self):
       pass

    @abstractmethod
    def get_response_for_create_update_test_case(
            self, test_case_dto: TestCaseDto):
        pass

    @abstractmethod
    def get_response_for_create_update_prefilled_codes(
            self, prefilled_codes_dto: List[PrefilledCodeDto]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_prefilled_code(self):
        pass

    @abstractmethod
    def get_response_for_create_update_clean_solutions(
            self, clean_solutions_dto: List[CleanSolutionDto]):
        pass

    @abstractmethod
    def raise_exception_for_invalid_clean_solution(self):
        pass

    @abstractmethod
    def get_response_for_create_update_solution_approach(
            self, solution_approach_dto: SolutionApproachDto):
        pass

    @abstractmethod
    def raise_exception_for_invalid_solution_approach(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_hint(self):
        pass

    @abstractmethod
    def get_response_for_create_update_hint(self, hint_dto: HintDto):
        pass

    @abstractmethod
    def raise_exception_for_offset_exception(self):
        pass

    @abstractmethod
    def raise_exception_for_limit_exception(self):
        pass

    @abstractmethod
    def raise_exception_for_solution_approach_exists(self):
        pass

    # Duplicate-ids

    @abstractmethod
    def raise_exception_for_duplicate_ids(self):
        pass
