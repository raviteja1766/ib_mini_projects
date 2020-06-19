from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .prefilled_code_storage_interface import PrefilledCodeStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin

class DeletePrefilledCodeInteractor(QuestionValidationMixin):

    def __init__(
            self, presenter: PresenterInterface,
            question_storage: QuestionStorageInterface,
            prefilled_code_storage: PrefilledCodeStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.prefilled_code_storage = prefilled_code_storage

    def delete_prefilled_code_to_question(
            self, question_id: int, prefilled_code_id: int):

        self.validate_question_id(question_id=question_id)
        is_invalid_prefilled_code = not self.prefilled_code_storage\
            .validate_prefilled_code(prefilled_code_id=prefilled_code_id)
        if is_invalid_prefilled_code:
            self.presenter.raise_exception_for_invalid_prefilled_code()
        prefilled_code_question_id = self.prefilled_code_storage\
            .get_question_to_prefilled_code(prefilled_code_id=prefilled_code_id)
        is_not_same_question = not prefilled_code_question_id == question_id
        if is_not_same_question:
            self.presenter.raise_exception_for_different_question()
        else:
            self.prefilled_code_storage.delete_prefilled_code(
                prefilled_code_id=prefilled_code_id
            )
