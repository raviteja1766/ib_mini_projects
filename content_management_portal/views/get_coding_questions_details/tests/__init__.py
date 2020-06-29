# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "get_coding_questions_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "coding_questions/v1/"

from .test_case_01 import TestCase01GetCodingQuestionsDetailsAPITestCase
from .test_case_02 import TestCase02GetCodingQuestionsDetailsAPITestCase
from .test_case_03 import TestCase03GetCodingQuestionsDetailsAPITestCase
from .test_case_04 import TestCase04GetCodingQuestionsDetailsAPITestCase
from .test_case_05 import TestCase05GetCodingQuestionsDetailsAPITestCase
from .test_case_06 import TestCase06GetCodingQuestionsDetailsAPITestCase

__all__ = [
    "TestCase01GetCodingQuestionsDetailsAPITestCase",
    "TestCase02GetCodingQuestionsDetailsAPITestCase",
    "TestCase03GetCodingQuestionsDetailsAPITestCase",
    "TestCase04GetCodingQuestionsDetailsAPITestCase",
    "TestCase05GetCodingQuestionsDetailsAPITestCase",
    "TestCase06GetCodingQuestionsDetailsAPITestCase"
]
