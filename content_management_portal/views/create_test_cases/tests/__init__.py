# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_test_cases"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/test_cases/v1/"

from .test_case_01 import TestCase01CreateTestCasesAPITestCase

__all__ = [
    "TestCase01CreateTestCasesAPITestCase"
]
