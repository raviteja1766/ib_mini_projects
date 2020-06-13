from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import TestCaseDto

class CreateUpdateTestCaseInteractor:

    def __init__(
            self, presenter: PresenterInterface,
            question_storage: QuestionStorageInterface,
            test_case_storage: TestCaseStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.test_case_storage = test_case_storage

    def create_update_test_case(self, test_case_dto: TestCaseDto):

        question_id = test_case_dto.question_id
        self._validations_for_question(question_id=question_id)
        is_update_test_case = not test_case_dto.id is None
        if is_update_test_case:
            self._validations_for_test_case(test_case_dto)
            test_case_dto = self.test_case_storage\
                .update_test_case(test_case_dto=test_case_dto)
        else:
            test_case_dto =\
            self._update_test_case_dto_order_and_create_test_case(test_case_dto)
        return self.presenter.get_response_for_create_update_test_case(
            test_case_dto=test_case_dto
        )

    def _update_test_case_dto_order_and_create_test_case(
            self, test_case_dto: TestCaseDto):

        question_id = test_case_dto.question_id
        max_order_id = self.test_case_storage\
            .get_max_test_case_order_of_question(question_id)
        is_zero_test_cases = max_order_id is None
        if is_zero_test_cases:
            max_order_id = 0
        test_case_dto.order_id = max_order_id + 1
        return self.test_case_storage\
            .create_test_case(test_case_dto=test_case_dto)

    def _validations_for_test_case(self, test_case_dto: TestCaseDto):

        is_invalid_test_case = not self.test_case_storage\
            .validate_test_case(test_case_id=test_case_dto.id)
        if is_invalid_test_case:
            self.presenter.raise_exception_for_invalid_test_case()
        test_case_question_id = self.test_case_storage\
            .get_question_to_test_case(test_case_id=test_case_dto.id)
        question_id = test_case_dto.question_id
        is_different_question = not test_case_question_id == question_id
        if is_different_question:
            self.presenter.raise_exception_for_different_question()

    def _validations_for_question(self, question_id: int):

        is_invalid_question = not self.question_storage\
            .validate_question_id(question_id=question_id)
        if is_invalid_question:
            self.presenter.raise_exception_for_invalid_question()


