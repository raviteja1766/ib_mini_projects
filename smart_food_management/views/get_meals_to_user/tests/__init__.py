# pylint: disable=wrong-import-position

APP_NAME = "smart_food_management"
OPERATION_NAME = "get_meals_to_user"
REQUEST_METHOD = "get"
URL_SUFFIX = "meals_info/v1/"

from .test_case_01 import TestCase01GetMealsToUserAPITestCase

__all__ = [
    "TestCase01GetMealsToUserAPITestCase"
]
