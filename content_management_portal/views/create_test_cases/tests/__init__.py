# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_test_cases"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/test_cases/v1/"

from .test_case_01 import TestCase01CreateTestCasesAPITestCase
from .test_case_02 import TestCase02CreateTestCasesAPITestCase
from .test_case_03 import TestCase03CreateTestCasesAPITestCase
from .test_case_04 import TestCase04CreateTestCasesAPITestCase

__all__ = [
    "TestCase01CreateTestCasesAPITestCase",
    "TestCase02CreateTestCasesAPITestCase",
    "TestCase03CreateTestCasesAPITestCase",
    "TestCase04CreateTestCasesAPITestCase"
]
