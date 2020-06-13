from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from typing import Dict, List
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.interactors.storages.dtos\
    import PrefilledCodeDto
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.prefilled_code_storage_implementation\
    import PrefilledCodeStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .create_update_prefilled_codes_interactor\
    import CreateUpdatePrefilledCodesInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = int(kwargs['question_id'])
    prefilled_codes_dict = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    prefilled_code_storage = PrefilledCodeStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateUpdatePrefilledCodesInteractor(
        question_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage)
    prefilled_codes_dto = _convert_prefilled_code_dict_to_dto(
        user_id=user.id, question_id=question_id,
        prefilled_codes_dict=prefilled_codes_dict)
    interactor_response = interactor\
        .create_update_prefilled_codes(question_id,prefilled_codes_dto)

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response

def _convert_prefilled_code_dict_to_dto(
        user_id: int, question_id: int, prefilled_codes_dict: List[Dict]):
    
    return [
        PrefilledCodeDto(
            id=prefilled_code_dict.get('prefilled_code_id'),
            file_name=prefilled_code_dict['file_name'],
            language_type=prefilled_code_dict['language'],
            text_code=prefilled_code_dict['solution_content'],
            question_id=question_id,
            user_id=user_id
        ) for prefilled_code_dict in prefilled_codes_dict
    ]