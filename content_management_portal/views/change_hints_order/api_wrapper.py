from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from typing import Dict
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.interactors.storages.dtos\
    import HintSwapDto
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .update_hints_order_interactor\
    import UpdateHintsOrderInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    question_id = int(kwargs['question_id'])
    hints_dict = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    hint_storage = HintStorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateHintsOrderInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage)
    hints_dto = _convert_hint_dict_to_dtos(
        question_id=question_id, hints_dict=hints_dict)
    interactor.update_hints_order(
        question_id=question_id, hints_dto=hints_dto
    )
    response = HttpResponse(status=200)
    return response

def _convert_hint_dict_to_dtos(
        question_id: int, hints_dict: Dict):

    return [
        HintSwapDto(
            id=hint_dict['hint_id'],
            order_id=hint_dict['hint_number']
        )
        for hint_dict in hints_dict.values()
    ]
