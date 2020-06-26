# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_question"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/statement/v1/"

from .test_case_01 import TestCase01CreateQuestionAPITestCase
from .test_case_02 import TestCase01CreateQuestionAPITestCase
from .test_case_03 import TestCase01CreateQuestionAPITestCase

__all__ = [
    "TestCase01CreateQuestionAPITestCase"
]
