# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_clean_solution_to_question"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/{question_id}/clean_solutions/{clean_solution_id}/v1/"

from .test_case_01 import TestCase01DeleteCleanSolutionToQuestionAPITestCase

__all__ = [
    "TestCase01DeleteCleanSolutionToQuestionAPITestCase"
]
