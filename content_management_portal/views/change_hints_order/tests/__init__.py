# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "change_hints_order"
REQUEST_METHOD = "put"
URL_SUFFIX = "coding_questions/{question_id}/hints/swap/v1/"

from .test_case_01 import TestCase01ChangeHintsOrderAPITestCase

__all__ = [
    "TestCase01ChangeHintsOrderAPITestCase"
]
