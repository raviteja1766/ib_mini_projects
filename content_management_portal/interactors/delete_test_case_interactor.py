from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin


class DeleteTestCaseInteractor(QuestionValidationMixin):

    def __init__(
            self, presenter: PresenterInterface,
            question_storage: QuestionStorageInterface,
            test_case_storage: TestCaseStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.test_case_storage = test_case_storage

    def delete_test_case_to_question(
            self, question_id: int, test_case_id: int):

        self.validate_question_id(question_id=question_id)
        is_invalid_test_case = not self.test_case_storage\
            .validate_test_case(test_case_id=test_case_id)
        if is_invalid_test_case:
            self.presenter.raise_exception_for_invalid_test_case()
        test_case_question_id = self.test_case_storage\
            .get_question_to_test_case(test_case_id=test_case_id)
        is_not_same_question = not test_case_question_id == question_id
        if is_not_same_question:
            self.presenter.raise_exception_for_different_question()
        else:
            self._delete_and_change_test_cases_order_to_question(
                question_id=question_id, test_case_id=test_case_id)


    def _delete_and_change_test_cases_order_to_question(
            self, question_id: int, test_case_id: int):
        order_id = self.test_case_storage\
            .delete_test_case_and_get_test_case_order(
                test_case_id=test_case_id)
        self.test_case_storage.update_questions_next_test_cases_order(
            question_id=question_id, order_id=order_id)
