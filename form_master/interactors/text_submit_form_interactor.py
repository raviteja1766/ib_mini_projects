

from form_master.interactors.base_submit_form_interactor \
    import BaseSubmitFormResponseInteractor
from form_master.interactors.storages.storage_interface \
    import StorageInterface
from form_master.exceptions.exceptions import InvalidUserResponseSubmit
from form_master.interactors.storages.dtos import UserTextResponseDTO


class TextQuestionSubmitFormResponseInteractor(
        BaseSubmitFormResponseInteractor):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int, user_submitted_text: int):
        super().__init__(storage, question_id, form_id, user_id)
        self.user_submitted_text = user_submitted_text

    def _validate_user_response(self):

        is_empty_text = not self.user_submitted_text
        if is_empty_text:
            raise InvalidUserResponseSubmit

    def _create_user_response(self) -> int:

        user_response_dto = UserTextResponseDTO(
            user_id=self.user_id,
            question_id=self.question_id,
            text=self.user_submitted_text
        )
        response_id = self.storage.create_user_text_response(
            user_response_dto=user_response_dto
        )
        return response_id

