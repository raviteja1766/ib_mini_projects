# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "delete_hint_to_question"
REQUEST_METHOD = "delete"
URL_SUFFIX = "coding_questions/{question_id}/hints/{hint_id}/v1/"

from .test_case_01 import TestCase01DeleteHintToQuestionAPITestCase

__all__ = [
    "TestCase01DeleteHintToQuestionAPITestCase"
]
