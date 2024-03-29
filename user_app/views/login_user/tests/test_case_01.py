"""
# TODO: Update test case description
"""
import datetime
from unittest.mock import patch
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from common.dtos import UserAuthTokensDTO
from user_app.models import User
from common.oauth_user_auth_tokens_service\
    import OAuthUserAuthTokensService

REQUEST_BODY = """
{
    "username": "raviteja",
    "password": "asdf1234"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase01LoginUserAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens')
    def test_case(self, mock_obj):
        mock_obj.return_value = UserAuthTokensDTO(
            user_id=1, access_token="1OfS6IZWCum8Jgpudp6FcAnqfKAb7t",
            refresh_token="SLnTl4l4z07mW7s96AlBcuXBhvVeid",
            expires_in=datetime.datetime(5189, 4, 11, 9, 51, 25, 278085)
        )
        user_obj = User.objects.create(username="raviteja")
        user_obj.set_password("asdf1234")
        user_obj.save()
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.