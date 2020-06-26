# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "get_coding_questions_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "coding_questions/v1/"

from .test_case_01 import TestCase01GetCodingQuestionsDetailsAPITestCase
from .test_case_02 import TestCase01GetCodingQuestionsDetailsAPITestCase
from .test_case_03 import TestCase01GetCodingQuestionsDetailsAPITestCase
from .test_case_04 import TestCase01GetCodingQuestionsDetailsAPITestCase
from .test_case_05 import TestCase01GetCodingQuestionsDetailsAPITestCase
from .test_case_06 import TestCase01GetCodingQuestionsDetailsAPITestCase

__all__ = [
    "TestCase01GetCodingQuestionsDetailsAPITestCase"
]
