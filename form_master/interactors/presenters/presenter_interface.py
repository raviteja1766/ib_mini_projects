from abc import ABC
from abc import abstractmethod
from typing import Optional, List, Dict
from form_master.exceptions.exceptions import FormDoesNotExist

class PresenterInterface(ABC):

    @abstractmethod
    def submit_form_response_return(self, response_id: int):
        pass

    @abstractmethod
    def raise_form_does_not_exist_exception(
            self, error_object: FormDoesNotExist):
        pass


    @abstractmethod
    def raise_form_closed_exception(self):
        pass

    @abstractmethod
    def raise_question_does_not_belong_to_form_exception(self):
        pass

    @abstractmethod
    def raise_invalid_user_response_submitted(self):
        pass