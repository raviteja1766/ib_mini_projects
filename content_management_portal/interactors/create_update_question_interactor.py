from content_management_portal.interactors.storages.dtos\
    import QuestionDto
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.constants.enums import DescriptionType
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin


class CreateUpdateQuestionInteractor(QuestionValidationMixin):

    def __init__(self, question_storage: QuestionStorageInterface,
                 presenter: PresenterInterface):
        self.question_storage = question_storage
        self.presenter = presenter

    def create_update_question(self, question_dto: QuestionDto):

        question_id = question_dto.id
        is_update_question = question_id
        if is_update_question:
            user_id = question_dto.user_id
            self._validations_for_question_and_user(user_id, question_id)
            question_dto = self.question_storage.update_question(question_dto)
        else:
            question_dto = self.question_storage.create_question(question_dto)
        return self.presenter.get_response_for_question_dto(
            question_dto=question_dto)


    def _validations_for_question_and_user(self, user_id, question_id):

        self.validate_question_id(question_id=question_id)

        question_user_id = self.question_storage\
            .get_user_to_question(question_id=question_id)

        is_different_user = not user_id == question_user_id
        if is_different_user:
            self.presenter.raise_exception_for_user_cannot_update_question()
