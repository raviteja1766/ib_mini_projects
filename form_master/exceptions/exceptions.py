

class FormClosed(Exception):
    pass


class FormDoesNotExist(Exception):
    def __init__(self, form_id: int):
        self.form_id = form_id


class QuestionDoesNotBelongToForm(Exception):
    pass


class InvalidUserResponseSubmit(Exception):
    pass

