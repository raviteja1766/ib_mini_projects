from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from typing import Dict, Any
from content_management_portal.interactors.storages.dtos\
    import QuestionDto
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation

from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors.create_update_question_interactor\
    import CreateUpdateQuestionInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_obj = kwargs['user']
    question_dict = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateUpdateQuestionInteractor(
        question_storage=question_storage, presenter=presenter
    )
    question_dto = _get_question_dto(user_obj.id, question_dict)
    interactor_response = interactor.create_update_question(
        question_dto=question_dto
    )
    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response


def _get_question_dto(
        user_id: int, question_dict: Dict[str, Any]) -> QuestionDto:
    
    return QuestionDto(
        id=question_dict.get('question_id'),
        short_text=question_dict['short_text'],
        text_type=question_dict['problem_description']['content_type'],
        description=question_dict['problem_description']['content'],
        created_at=None,
        user_id=user_id
    )