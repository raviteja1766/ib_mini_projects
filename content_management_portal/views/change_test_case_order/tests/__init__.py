# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "change_test_case_order"
REQUEST_METHOD = "put"
URL_SUFFIX = "coding_questions/{question_id}/test_cases/swap/v1/"

from .test_case_01 import TestCase01ChangeTestCaseOrderAPITestCase

__all__ = [
    "TestCase01ChangeTestCaseOrderAPITestCase"
]
