# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_hints_to_question"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/hints/v1/"

from .test_case_01 import TestCase01CreateHintsToQuestionAPITestCase

__all__ = [
    "TestCase01CreateHintsToQuestionAPITestCase"
]
