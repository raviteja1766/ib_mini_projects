from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from typing import Dict
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.interactors.storages.dtos\
    import TestCaseDto
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.test_case_storage_implementation\
    import TestCaseStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .create_update_test_case_interactor\
    import CreateUpdateTestCaseInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = int(kwargs['question_id'])
    test_case_dict = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    test_case_storage = TestCaseStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateUpdateTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage)
    test_case_dto = _convert_test_case_dict_to_dto(
        user_id=user.id, question_id=question_id,
        test_case_dict=test_case_dict)
    interactor_response = interactor\
        .create_update_test_case(test_case_dto=test_case_dto)

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response

def _convert_test_case_dict_to_dto(
        user_id: int, question_id: int, test_case_dict: Dict):
    
    return TestCaseDto(
        id=test_case_dict.get('test_case_id'),
        input_text=test_case_dict['input'],
        output_text=test_case_dict['output'],
        score=test_case_dict['score'],
        is_hidden=test_case_dict['is_hidden'],
        order_id=test_case_dict.get('test_case_number'),
        question_id=question_id,
        user_id=user_id
    )