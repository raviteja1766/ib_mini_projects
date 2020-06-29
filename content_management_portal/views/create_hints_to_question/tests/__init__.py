# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_hints_to_question"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/hints/v1/"

from .test_case_01 import TestCase01CreateHintsToQuestionAPITestCase
from .test_case_02 import TestCase02CreateHintsToQuestionAPITestCase
from .test_case_03 import TestCase03CreateHintsToQuestionAPITestCase
from .test_case_04 import TestCase04CreateHintsToQuestionAPITestCase

__all__ = [
    "TestCase01CreateHintsToQuestionAPITestCase",
    "TestCase02CreateHintsToQuestionAPITestCase",
    "TestCase03CreateHintsToQuestionAPITestCase",
    "TestCase04CreateHintsToQuestionAPITestCase"
]
