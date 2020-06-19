from django_swagger_utils.drf_server.exceptions import (
    NotFound, Unauthorized, Forbidden, BadRequest
)
from abc import ABC
from abc import abstractmethod
from typing import List
from common.dtos import UserAuthTokensDTO
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages.dtos\
    import (
        RoughSolutionDto, CodingQuestionDto,
        QuestionDto, TestCaseDto, PrefilledCodeDto, CleanSolutionDto,
        SolutionApproachDto, HintDto
    )
from content_management_portal.constants.exception_messages import *


class PresenterImplementation(PresenterInterface):

    def get_response_for_login_user(
            self, user_auth_token_dto: UserAuthTokensDTO):

        return {
            "user_id": user_auth_token_dto.user_id,
            "access_token": user_auth_token_dto.access_token,
            "refresh_token": user_auth_token_dto.refresh_token,
            "expires_in": str(user_auth_token_dto.expires_in)
        }

    def raise_exception_for_invalid_question(self):

        raise NotFound(*INVALID_QUESTION_EXCEPTION)

    def raise_exception_for_invalid_username(self):

        raise Unauthorized(*INVALID_USERNAME_EXCEPTION)

    def raise_exception_for_invalid_password(self):

        raise Unauthorized(*INVALID_PASSWORD_EXCEPTION)

    def get_response_for_question_dto(self, question_dto: QuestionDto):

        question_dto_dict = {
            "question_id": question_dto.id
        }
        problem_statement_dict = \
            self._get_problem_statement_to_question_dto(question_dto)
        question_dto_dict.update(problem_statement_dict)

        return question_dto_dict

    @staticmethod
    def _get_problem_statement_to_question_dto(question_dto):

        return {
            "short_text": question_dto.short_text,
            "problem_description": {
                "content_type": question_dto.text_type,
                "content": question_dto.description
            }
        }

    def raise_exception_for_user_cannot_delete_question(self):

        raise Forbidden(*USER_CANNOT_DELETE_QUESTION_EXCEPTION)

    def raise_exception_for_rough_solution_not_in_question(self):

        raise Forbidden(*INVALID_QUESTION_EXCEPTION)

    def raise_exception_for_invalid_rough_solution(self):

        raise NotFound(*INVALID_ROUGH_SOLUTION_EXCEPTION)

    def get_response_for_create_update_rough_solutions(
            self, rough_solutions_dto: List[RoughSolutionDto]):

        question_id = rough_solutions_dto[0].question_id
        return {
            "question_id": question_id,
            "rough_solutions":\
            self._convert_rough_solutions_dto_to_dict(rough_solutions_dto)
        }
    
    @staticmethod
    def _convert_rough_solutions_dto_to_dict(rough_solutions_dto):
    
        return [
            {
                "rough_solution_id": rough_solution.id,
                "file_name": rough_solution.file_name,
                "language": rough_solution.language_type,
                "solution_content": rough_solution.text_code
            }
            for rough_solution in rough_solutions_dto
        ]

    def raise_exception_for_user_cannot_update_question(self):

        raise Forbidden(*USER_CANNOT_UPDATE_QUESTION_EXCEPTION)

    def raise_exception_for_different_question(self):

        raise Forbidden(*INVALID_QUESTION_EXCEPTION)

    def get_response_for_get_coding_questions_details(
            self,offset: int, limit: int, questions_count: int,
            coding_questions_dto: List[CodingQuestionDto]):

        return {
            "total_questions": questions_count,
            "offset": offset,
            "limit": limit,
            "questions_list": [
                self._convert_codingquestion_dto_to_dict(coding_question_dto)
                for coding_question_dto in coding_questions_dto
            ]
        }
    
    @staticmethod
    def _convert_codingquestion_dto_to_dict(coding_question_dto):
        
        return {
            "question_id": coding_question_dto.question_id,
            "statement": coding_question_dto.short_text,
            "rough_solution_status": coding_question_dto.rough_solutions,
            "test_cases_status": coding_question_dto.test_cases,
            "prefilled_code_status": coding_question_dto.prefilled_code,
            "solution_approach_status": \
                coding_question_dto.solution_approach,
            "clean_solution_status": coding_question_dto.clean_solution
        }

    def get_response_for_complete_question_details(
            self, question_dto, rough_solutions_dto, test_cases_dto,
            prefilled_codes_dto, solution_approach_dto,
            clean_solutions_dto, hints_dto):

        return {
            "question_id": question_dto.id,
            "statement": self._get_problem_statement_to_question_dto(
                question_dto=question_dto
            ),
            "rough_solutions":
            self._convert_rough_solutions_dto_to_dict(rough_solutions_dto),
            "test_cases": [
                self._convert_test_case_dto_to_dict(test_case_dto)
                for test_case_dto in test_cases_dto
            ],
            "prefilled_codes":
            self._convert_prefilled_codes_dto_to_dict(prefilled_codes_dto),
            "solution_approach":
            self._convert_solution_approach_dto_to_dict(solution_approach_dto),
            "clean_solutions":
            self._convert_clean_solutions_dto_to_dict(clean_solutions_dto),
            "hints": [
                self._convert_hint_dto_to_dict(hint_dto=hint_dto)
                for hint_dto in hints_dto
            ]
        }

    def raise_exception_for_invalid_test_case(self):

        raise NotFound(*INVALID_TESTCASE_EXCEPTION)

    def get_response_for_create_update_test_case(
            self, test_case_dto: TestCaseDto):

        return {
            "question_id": test_case_dto.question_id,
            "test_case": self._convert_test_case_dto_to_dict(test_case_dto)
        }
    
    @staticmethod
    def _convert_test_case_dto_to_dict(test_case_dto):
        return {
            "test_case_id": test_case_dto.id,
            "input": test_case_dto.input_text,
            "output": test_case_dto.output_text,
            "score": test_case_dto.score,
            "is_hidden": test_case_dto.is_hidden,
            "test_case_number": test_case_dto.order_id
        }

    def raise_exception_for_invalid_prefilled_code(self):

        raise NotFound(*INVALID_PREFILLED_CODE_EXCEPTION)

    def get_response_for_create_update_prefilled_codes(
            self, prefilled_codes_dto: List[PrefilledCodeDto]):

        question_id = prefilled_codes_dto[0].question_id
        return {
            "question_id": question_id,
            "prefilled_codes":\
            self._convert_prefilled_codes_dto_to_dict(prefilled_codes_dto)
        }

    @staticmethod
    def _convert_prefilled_codes_dto_to_dict(prefilled_codes_dto):
        return [
            {
                "prefilled_code_id": prefilled_code_dto.id,
                "file_name": prefilled_code_dto.file_name,
                "language": prefilled_code_dto.language_type,
                "solution_content": prefilled_code_dto.text_code
            }
            for prefilled_code_dto in prefilled_codes_dto
        ]

    def raise_exception_for_invalid_clean_solution(self):

        raise NotFound(*INVALID_CLEAN_SOLUTION_EXCEPTION)

    def get_response_for_create_update_clean_solutions(
            self, clean_solutions_dto: List[CleanSolutionDto]):

        question_id = clean_solutions_dto[0].question_id
        return {
            "question_id": question_id,
            "clean_solutions":
            self._convert_clean_solutions_dto_to_dict(clean_solutions_dto)
        }

    @staticmethod
    def _convert_clean_solutions_dto_to_dict(clean_solutions_dto):
        return [
            {
                "clean_solution_id": clean_solution_dto.id,
                "file_name": clean_solution_dto.file_name,
                "language": clean_solution_dto.language_type,
                "solution_content": clean_solution_dto.text_code
            }
            for clean_solution_dto in clean_solutions_dto
        ]

    def get_response_for_create_update_solution_approach(
            self, solution_approach_dto: SolutionApproachDto):

        return {
            "question_id": solution_approach_dto.question_id,
            "solution_approach":
            self._convert_solution_approach_dto_to_dict(solution_approach_dto)
        }

    @staticmethod
    def _convert_solution_approach_dto_to_dict(solution_approach_dto):
        
        if solution_approach_dto is None:
            return None
        return {
            "solution_approach_id": solution_approach_dto.id,
            "title": solution_approach_dto.title,
            "description": {
              "content_type": solution_approach_dto.description_content_type,
              "content": solution_approach_dto.description_content
            },
            "complexity_analysis": {
              "content_type": solution_approach_dto.complexity_content_type,
              "content": solution_approach_dto.complexity_content
            }
        }

    def raise_exception_for_invalid_solution_approach(self):

        raise NotFound(*INVALID_SOLUTION_APPROACH_EXCEPTION)

    def raise_exception_for_invalid_hint(self):

        raise NotFound(*INVALID_HINT_EXCEPTION)

    def get_response_for_create_update_hint(self, hint_dto: HintDto):

        return {
            "question_id": hint_dto.question_id,
            "hint": self._convert_hint_dto_to_dict(hint_dto)
        }

    @staticmethod
    def _convert_hint_dto_to_dict(hint_dto):

        return {
            "hint_id": hint_dto.id,
            "title": hint_dto.title,
            "description": {
                "content_type": hint_dto.content_type,
                "content": hint_dto.content
            },
            "hint_number": hint_dto.order_id
        }

    def raise_exception_for_offset_exception(self):

        raise BadRequest(*INVALID_OFFSET_LENGTH)

    def raise_exception_for_limit_exception(self):

        raise BadRequest(*INVALID_LIMIT_LENGTH)

    def raise_exception_for_solution_approach_exists(self):

        raise BadRequest(*SOLUTION_APPROACH_ALREADY_EXISTS)

    def raise_exception_for_duplicate_ids(self):

        raise BadRequest(*DUPLICATE_IDS_EXCEPTION)
