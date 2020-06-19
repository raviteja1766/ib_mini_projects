



class QuestionValidationMixin:

    def validate_question_id(self, question_id: int):
        is_invalid_question = not self.question_storage\
            .validate_question_id(question_id=question_id)
        if is_invalid_question:
            self.presenter.raise_exception_for_invalid_question()