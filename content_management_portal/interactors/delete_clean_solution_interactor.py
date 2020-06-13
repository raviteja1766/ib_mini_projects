from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .clean_solution_storage_interface import CleanSolutionStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface


class DeleteCleanSolutionInteractor:

    def __init__(
            self, presenter: PresenterInterface,
            question_storage: QuestionStorageInterface,
            clean_solution_storage: CleanSolutionStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.clean_solution_storage = clean_solution_storage

    def delete_clean_solution_to_question(
            self, question_id: int, clean_solution_id: int):

        is_invalid_question = not self.question_storage.validate_question_id(
            question_id=question_id)
        if is_invalid_question:
            self.presenter.raise_exception_for_invalid_question()
        is_invalid_clean_solution = not self.clean_solution_storage\
            .validate_clean_solution(clean_solution_id=clean_solution_id)
        if is_invalid_clean_solution:
            self.presenter.raise_exception_for_invalid_clean_solution()
        clean_solution_question_id = self.clean_solution_storage\
            .get_question_to_clean_solution(clean_solution_id=clean_solution_id)
        is_not_same_question = not clean_solution_question_id == question_id
        if is_not_same_question:
            self.presenter.raise_exception_for_different_question()
        else:
            self.clean_solution_storage.delete_clean_solution(
                clean_solution_id=clean_solution_id
            )
