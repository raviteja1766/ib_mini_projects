# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_prefilled_code_to_question"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/{question_id}/prefilled_codes/{prefilled_code_id}/v1/"

from .test_case_01 import TestCase01DeletePrefilledCodeToQuestionAPITestCase
from .test_case_02 import TestCase02DeletePrefilledCodeToQuestionAPITestCase
from .test_case_03 import TestCase03DeletePrefilledCodeToQuestionAPITestCase
from .test_case_04 import TestCase04DeletePrefilledCodeToQuestionAPITestCase

__all__ = [
    "TestCase01DeletePrefilledCodeToQuestionAPITestCase",
    "TestCase02DeletePrefilledCodeToQuestionAPITestCase",
    "TestCase03DeletePrefilledCodeToQuestionAPITestCase",
    "TestCase04DeletePrefilledCodeToQuestionAPITestCase"
]
