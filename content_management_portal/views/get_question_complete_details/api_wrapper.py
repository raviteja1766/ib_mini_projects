from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation

from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .get_complete_question_details_interactor\
    import GetQuestionCompleteDetailsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs['question_id']
    question_storage = QuestionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetQuestionCompleteDetailsInteractor(
        question_storage=question_storage, presenter=presenter
    )
    interactor_response = interactor.get_complete_question_details(
        question_id=question_id
    )

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=200)
    return response