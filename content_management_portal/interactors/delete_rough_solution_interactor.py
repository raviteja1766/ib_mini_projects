from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages\
    .rough_solution_storage_interface import RoughSolutionStorageInterface
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin


class DeleteRoughSolutionInteractor(QuestionValidationMixin):

    def __init__(self, question_storage: QuestionStorageInterface,
                 rough_storage: RoughSolutionStorageInterface,
                 presenter: PresenterInterface):
        self.question_storage = question_storage
        self.rough_storage = rough_storage
        self.presenter = presenter

    def delete_rough_solution_to_question(self, question_id: int,
                                          rough_solution_id: int):

        self.validate_question_id(question_id=question_id)
        is_invalid_rough_solution = not self.rough_storage\
            .validate_rough_solution_id(rough_solution_id=rough_solution_id)
        if is_invalid_rough_solution:
            self.presenter.raise_exception_for_invalid_rough_solution()
        rough_solutions_question_id = self.rough_storage\
            .get_question_to_rough_solution(rough_solution_id)
        is_not_same_question = not rough_solutions_question_id == question_id
        if is_not_same_question:
            self.presenter.raise_exception_for_rough_solution_not_in_question()
        else:
            self.rough_storage.delete_rough_solution(
                rough_solution_id=rough_solution_id)
