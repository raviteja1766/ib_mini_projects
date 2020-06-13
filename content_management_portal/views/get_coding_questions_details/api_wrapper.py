from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation

from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors.get_coding_questions_interactor\
    import GetCodingQuestionsInteractors


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_storage = QuestionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetCodingQuestionsInteractors(
        question_storage=question_storage, presenter=presenter
    )
    query_params = kwargs['request_query_params']
    offset = query_params.offset
    limit = query_params.limit
    interactor_response = interactor.get_coding_questions_details(
        offset=offset, limit=limit
    )
    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=200)
    return response