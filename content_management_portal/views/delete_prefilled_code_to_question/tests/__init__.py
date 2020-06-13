# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_prefilled_code_to_question"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/{question_id}/prefilled_codes/{prefilled_code_id}/v1/"

from .test_case_01 import TestCase01DeletePrefilledCodeToQuestionAPITestCase

__all__ = [
    "TestCase01DeletePrefilledCodeToQuestionAPITestCase"
]
