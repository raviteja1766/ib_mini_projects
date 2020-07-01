# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_rough_solutions"
REQUEST_METHOD = "post"
URL_SUFFIX = "coding_questions/{question_id}/rough_solutions/v1/"

from .test_case_01 import TestCase01CreateRoughSolutionsAPITestCase
from .test_case_02 import TestCase02CreateRoughSolutionsAPITestCase
from .test_case_03 import TestCase03CreateRoughSolutionsAPITestCase
from .test_case_04 import TestCase04CreateRoughSolutionsAPITestCase
from .test_case_05 import TestCase05CreateRoughSolutionsAPITestCase

__all__ = [
    "TestCase01CreateRoughSolutionsAPITestCase",
    "TestCase02CreateRoughSolutionsAPITestCase",
    "TestCase03CreateRoughSolutionsAPITestCase",
    "TestCase04CreateRoughSolutionsAPITestCase",
    "TestCase05CreateRoughSolutionsAPITestCase"
]
