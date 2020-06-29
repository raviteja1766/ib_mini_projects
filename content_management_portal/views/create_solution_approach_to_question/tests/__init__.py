# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_solution_approach_to_question"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/solution_approaches/v1/"

from .test_case_01 import TestCase01CreateSolutionApproachToQuestionAPITestCase
from .test_case_02 import TestCase02CreateSolutionApproachToQuestionAPITestCase
from .test_case_03 import TestCase03CreateSolutionApproachToQuestionAPITestCase
from .test_case_04 import TestCase04CreateSolutionApproachToQuestionAPITestCase

__all__ = [
    "TestCase01CreateSolutionApproachToQuestionAPITestCase",
    "TestCase02CreateSolutionApproachToQuestionAPITestCase",
    "TestCase03CreateSolutionApproachToQuestionAPITestCase",
    "TestCase04CreateSolutionApproachToQuestionAPITestCase"
]
