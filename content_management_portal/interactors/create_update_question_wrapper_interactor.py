from content_management_portal.interactors.storages.dtos\
    import QuestionDto
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.constants.enums import DescriptionType


class InvalidQuestionId(Exception):
    pass


class UserCannotUpdateQuestion(Exception):
    pass

class CreateUpdateQuestionInteractor:

    def __init__(self, question_storage: QuestionStorageInterface):
        self.question_storage = question_storage


    def create_update_question_wrapper(self, question_dto: QuestionDto,
                                       presenter: PresenterInterface):

        try:
            question_dto = self.create_update_question(
                question_dto=question_dto
            )
        except InvalidQuestionId:
            presenter.raise_exception_for_invalid_question()
        except UserCannotUpdateQuestion:
            presenter.raise_exception_for_user_cannot_update_question()
        return presenter\
            .get_response_for_question_dto(question_dto=question_dto)

    def create_update_question(self, question_dto: QuestionDto):

        question_id = question_dto.id
        is_update_question = question_id
        if is_update_question:
            user_id = question_dto.user_id
            self._validations_for_question_and_user(user_id, question_id)
            question_dto = self.question_storage.update_question(question_dto)
        else:
            question_dto = self.question_storage.create_question(question_dto)
        return question_dto


    def _validations_for_question_and_user(self, user_id, question_id):

        is_invalid_question = not self.question_storage\
            .validate_question_id(question_id=question_id)
        if is_invalid_question:
            raise InvalidQuestionId()
        question_user_id = self.question_storage\
            .get_user_to_question(question_id=question_id)

        is_different_user = not user_id == question_user_id
        if is_different_user:
            raise UserCannotUpdateQuestion()
