from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors.delete_hint_interactor\
    import DeleteHintInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = int(kwargs['question_id'])
    hint_id = int(kwargs['hint_id'])
    question_storage = QuestionStorageImplementation()
    hint_storage = HintStorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteHintInteractor(
        question_storage=question_storage, presenter=presenter,
        hint_storage=hint_storage
    )

    interactor.delete_hint_to_question(
        question_id=question_id, hint_id=hint_id
    )
    response = HttpResponse(status=200)
    return response
