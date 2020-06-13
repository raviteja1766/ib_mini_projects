# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_rough_solution_to_question"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/{question_id}/rough_solutions/{rough_solution_id}/v1/"

from .test_case_01 import TestCase01DeleteRoughSolutionToQuestionAPITestCase

__all__ = [
    "TestCase01DeleteRoughSolutionToQuestionAPITestCase"
]
