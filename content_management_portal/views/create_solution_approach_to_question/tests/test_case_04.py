"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from content_management_portal.utils.custom_test_utils_2 \
    import CustomTestUtils

REQUEST_BODY = """
{
    "solution_approach_id": 1,
    "title": "string",
    "description": {
        "content_type": "HTML",
        "content": "string"
    },
    "complexity_analysis": {
        "content_type": "HTML",
        "content": "string"
    }
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"question_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01CreateSolutionApproachToQuestionAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01CreateSolutionApproachToQuestionAPITestCase, self).setupUser(
            username=username, password=password
        )
        self.reset_factory_sequence()
        self.create_users()
        self.create_questions()
        self.create_solution_approach()

    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.