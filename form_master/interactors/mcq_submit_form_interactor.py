

from form_master.interactors.base_submit_form_interactor \
    import BaseSubmitFormResponseInteractor
from form_master.interactors.storages.storage_interface \
    import StorageInterface
from form_master.exceptions.exceptions import InvalidUserResponseSubmit
from form_master.interactors.storages.dtos import UserResponseDTO


class MCQQuestionSubmitFormResponseInteractor(
        BaseSubmitFormResponseInteractor):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int, user_submitted_option_id: int):
        super().__init__(storage, question_id, form_id, user_id)
        self.user_submitted_option_id = user_submitted_option_id

    def _validate_user_response(self):

        option_ids = self.storage.get_option_ids_for_question(
            question_id=self.question_id
        )

        if self.user_submitted_option_id not in option_ids:
            raise InvalidUserResponseSubmit

    def _create_user_response(self) -> int:

        user_response_dto = UserResponseDTO(
            user_id=self.user_id,
            question_id=self.question_id,
            option_id=self.user_submitted_option_id
        )
        response_id = self.storage.create_user_mcq_response(
            user_response_dto=user_response_dto
        )
        return response_id

