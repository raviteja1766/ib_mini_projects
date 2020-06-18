from abc import abstractmethod
from form_master.interactors.storages.storage_interface \
    import StorageInterface
from form_master.interactors.presenters.presenter_interface \
    import PresenterInterface
from form_master.interactors.mixins.form_validation import FormValidationMixin
from form_master.exceptions.exceptions import *


class BaseSubmitFormResponseInteractor(FormValidationMixin):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int):
        self.storage = storage
        self.question_id = question_id
        self.form_id = form_id
        self.user_id = user_id

    def submit_form_response_wrapper(self, presenter: PresenterInterface):
        try:
            user_response_id = self.submit_form_response()
            return presenter.submit_form_response_return(
                response_id=user_response_id
            )
        except FormDoesNotExist as err_obj:
            presenter.raise_form_does_not_exist_exception(error_object=err_obj)
        except FormClosed:
            presenter.raise_form_closed_exception()
        except QuestionDoesNotBelongToForm:
            presenter.raise_question_does_not_belong_to_form_exception()
        except InvalidUserResponseSubmit:
            presenter.raise_invalid_user_response_submitted()

    def submit_form_response(self):
        self.validate_for_live_form(form_id=self.form_id)
        self.storage.validate_question_id_with_form(
            question_id=self.question_id, form_id=self.form_id
        )

        self._validate_user_response()
        user_response_id = self._create_user_response()

        return user_response_id

    @abstractmethod
    def _validate_user_response(self):
        pass

    @abstractmethod
    def _create_user_response(self) -> int:
        pass
