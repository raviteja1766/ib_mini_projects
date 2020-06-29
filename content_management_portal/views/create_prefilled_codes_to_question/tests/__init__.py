# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_prefilled_codes_to_question"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/prefilled_codes/v1/"

from .test_case_01 import TestCase01CreatePrefilledCodesToQuestionAPITestCase
from .test_case_02 import TestCase02CreatePrefilledCodesToQuestionAPITestCase
from .test_case_03 import TestCase03CreatePrefilledCodesToQuestionAPITestCase
from .test_case_04 import TestCase04CreatePrefilledCodesToQuestionAPITestCase

__all__ = [
    "TestCase01CreatePrefilledCodesToQuestionAPITestCase",
    "TestCase02CreatePrefilledCodesToQuestionAPITestCase",
    "TestCase03CreatePrefilledCodesToQuestionAPITestCase",
    "TestCase04CreatePrefilledCodesToQuestionAPITestCase"
]
