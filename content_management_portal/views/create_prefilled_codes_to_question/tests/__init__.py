# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_prefilled_codes_to_question"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/prefilled_codes/v1/"

from .test_case_01 import TestCase01CreatePrefilledCodesToQuestionAPITestCase

__all__ = [
    "TestCase01CreatePrefilledCodesToQuestionAPITestCase"
]
