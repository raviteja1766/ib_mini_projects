# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_solution_approach_to_question"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/solution_approaches/v1/"

from .test_case_01 import TestCase01CreateSolutionApproachToQuestionAPITestCase

__all__ = [
    "TestCase01CreateSolutionApproachToQuestionAPITestCase"
]
