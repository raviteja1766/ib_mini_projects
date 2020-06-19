from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .hint_storage_interface import HintStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin

class DeleteHintInteractor(QuestionValidationMixin):

    def __init__(
            self, presenter: PresenterInterface,
            question_storage: QuestionStorageInterface,
            hint_storage: HintStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.hint_storage = hint_storage

    def delete_hint_to_question(
            self, question_id: int, hint_id: int):

        self.validate_question_id(question_id=question_id)

        is_invalid_hint = not self.hint_storage\
            .validate_hint(hint_id=hint_id)
        if is_invalid_hint:
            self.presenter.raise_exception_for_invalid_hint()
        hint_question_id = self.hint_storage\
            .get_question_to_hint(hint_id=hint_id)
        is_not_same_question = not hint_question_id == question_id
        if is_not_same_question:
            self.presenter.raise_exception_for_different_question()
        else:
            order_id = self.hint_storage.delete_hint_and_get_hint_order(
                hint_id=hint_id)
            self.hint_storage.update_questions_next_hints_order(
                question_id=question_id, order_id=order_id)
