from typing import List, Dict
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import TestCaseSwapDto
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin


class UpdateTestCasesOrderInteractor(QuestionValidationMixin):

    def __init__(
            self, presenter: PresenterInterface,
            question_storage: QuestionStorageInterface,
            test_case_storage: TestCaseStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.test_case_storage = test_case_storage

    def update_test_cases_order(
            self, question_id: int, test_cases_dto: List[TestCaseSwapDto]):

        self.validate_question_id(question_id=question_id)
        self._validations_for_test_cases_dto(question_id, test_cases_dto)
        test_cases_dto = self.swap_test_cases_dto_order_id(test_cases_dto)
        self.test_case_storage.update_test_cases_order(test_cases_dto)

    def _validations_for_test_cases_dto(
            self, question_id: int, test_cases_dto: List[TestCaseSwapDto]):

        test_case_ids = [
            test_case_dto.id for test_case_dto in test_cases_dto
        ]
        db_test_case_ids = self.test_case_storage\
            .get_database_test_case_ids(test_case_ids)
        sorted_test_case_ids = sorted(test_case_ids)
        is_invalid_test_case = (
            not db_test_case_ids == sorted_test_case_ids
        )
        if is_invalid_test_case:
            self.presenter.raise_exception_for_invalid_test_case()

        self._validations_for_test_cases_questions(
            question_id=question_id,
            test_case_ids=test_case_ids
        )

    def _validations_for_test_cases_questions(
            self, question_id: int,test_case_ids: List[int]):

        test_case_question_ids = self.test_case_storage\
            .get_test_cases_question_ids(test_case_ids)
        is_different_question =\
            not test_case_question_ids == [question_id]
        if is_different_question:
            self.presenter.raise_exception_for_different_question()

    def swap_test_cases_dto_order_id(
            self, test_cases_dto: List[TestCaseSwapDto]):

        first_test_case_dto = test_cases_dto[0]
        second_test_case_dto = test_cases_dto[-1]
        temp_order_id = first_test_case_dto.order_id
        first_test_case_dto.order_id = second_test_case_dto.order_id
        second_test_case_dto.order_id =temp_order_id
    
        test_cases_dto = [first_test_case_dto, second_test_case_dto]
        return test_cases_dto