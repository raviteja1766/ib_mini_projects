# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_clean_solutions_to_question"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/clean_solutions/v1/"

from .test_case_01 import TestCase01CreateCleanSolutionsToQuestionAPITestCase
from .test_case_02 import TestCase02CreateCleanSolutionsToQuestionAPITestCase
from .test_case_03 import TestCase03CreateCleanSolutionsToQuestionAPITestCase
from .test_case_04 import TestCase04CreateCleanSolutionsToQuestionAPITestCase

__all__ = [
    "TestCase01CreateCleanSolutionsToQuestionAPITestCase",
    "TestCase02CreateCleanSolutionsToQuestionAPITestCase",
    "TestCase03CreateCleanSolutionsToQuestionAPITestCase",
    "TestCase04CreateCleanSolutionsToQuestionAPITestCase"
]
