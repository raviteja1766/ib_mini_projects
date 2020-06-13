# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "login_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "login/v1/"

from .test_case_01 import TestCase01LoginUserAPITestCase

__all__ = [
    "TestCase01LoginUserAPITestCase"
]
