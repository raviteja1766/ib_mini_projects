# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_rough_solution_to_question"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/{question_id}/rough_solutions/{rough_solution_id}/v1/"

from .test_case_01 import TestCase01DeleteRoughSolutionToQuestionAPITestCase
from .test_case_02 import TestCase02DeleteRoughSolutionToQuestionAPITestCase
from .test_case_03 import TestCase03DeleteRoughSolutionToQuestionAPITestCase
from .test_case_04 import TestCase04DeleteRoughSolutionToQuestionAPITestCase

__all__ = [
    "TestCase01DeleteRoughSolutionToQuestionAPITestCase",
    "TestCase02DeleteRoughSolutionToQuestionAPITestCase",
    "TestCase03DeleteRoughSolutionToQuestionAPITestCase",
    "TestCase04DeleteRoughSolutionToQuestionAPITestCase"
]
