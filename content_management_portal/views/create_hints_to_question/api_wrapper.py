from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from typing import Dict
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.interactors.storages.dtos\
    import HintDto
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .create_update_hint_interactor\
    import CreateUpdateHintInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = int(kwargs['question_id'])
    hint_dict = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    hint_storage = HintStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateUpdateHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage)
    hint_dto = _convert_hint_dict_to_dto(
        user_id=user.id, question_id=question_id, hint_dict=hint_dict)
    interactor_response = interactor.create_update_hint(hint_dto=hint_dto)

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response

def _convert_hint_dict_to_dto(
        user_id: int, question_id: int, hint_dict: Dict):

    return HintDto(
        id=hint_dict.get('hint_id'),
        title=hint_dict['title'],
        content_type=hint_dict['description']['content_type'],
        content=hint_dict['description']['content'],
        order_id=hint_dict.get('hint_number'),
        question_id=question_id, user_id=user_id
    )
