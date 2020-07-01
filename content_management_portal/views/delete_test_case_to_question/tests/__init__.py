# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_test_case_to_question"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/{question_id}/test_cases/{test_case_id}/v1/"

from .test_case_01 import TestCase01DeleteTestCaseToQuestionAPITestCase
from .test_case_02 import TestCase02DeleteTestCaseToQuestionAPITestCase
from .test_case_03 import TestCase03DeleteTestCaseToQuestionAPITestCase
from .test_case_04 import TestCase04DeleteTestCaseToQuestionAPITestCase

__all__ = [
    "TestCase01DeleteTestCaseToQuestionAPITestCase",
    "TestCase02DeleteTestCaseToQuestionAPITestCase",
    "TestCase03DeleteTestCaseToQuestionAPITestCase",
    "TestCase04DeleteTestCaseToQuestionAPITestCase"
]
