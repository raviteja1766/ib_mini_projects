from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.prefilled_code_storage_implementation\
    import PrefilledCodeStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .delete_prefilled_code_interactor\
    import DeletePrefilledCodeInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = int(kwargs['question_id'])
    prefilled_code_id = int(kwargs['prefilled_code_id'])
    question_storage = QuestionStorageImplementation()
    prefilled_code_storage = PrefilledCodeStorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeletePrefilledCodeInteractor(
        question_storage=question_storage, presenter=presenter,
        prefilled_code_storage=prefilled_code_storage
    )

    interactor.delete_prefilled_code_to_question(
        question_id=question_id, prefilled_code_id=prefilled_code_id
    )
    response = HttpResponse(status=200)
    return response
