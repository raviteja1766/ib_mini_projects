from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from typing import Dict
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.interactors.storages.dtos\
    import TestCaseSwapDto
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.test_case_storage_implementation\
    import TestCaseStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .update_test_cases_order_interactor\
    import UpdateTestCasesOrderInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    question_id = int(kwargs['question_id'])
    test_cases_dict = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    test_case_storage = TestCaseStorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateTestCasesOrderInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage)
    test_cases_dto = _convert_test_case_dict_to_dtos(
        question_id=question_id, test_cases_dict=test_cases_dict)
    interactor.update_test_cases_order(
        question_id=question_id, test_cases_dto=test_cases_dto
    )
    response = HttpResponse(status=200)
    return response

def _convert_test_case_dict_to_dtos(
        question_id: int, test_cases_dict: Dict):

    return [
        TestCaseSwapDto(
            id=test_case_dict['test_case_id'],
            order_id=test_case_dict['test_case_number']
        )
        for test_case_dict in test_cases_dict.values()
    ]
