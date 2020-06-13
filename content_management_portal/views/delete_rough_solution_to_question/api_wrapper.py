from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.rough_storage_implementation\
    import RoughSolutionStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .delete_rough_solution_interactor\
    import DeleteRoughSolutionInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = int(kwargs['question_id'])
    rough_solution_id = int(kwargs['rough_solution_id'])
    question_storage = QuestionStorageImplementation()
    rough_storage = RoughSolutionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteRoughSolutionInteractor(
        question_storage=question_storage, presenter=presenter,
        rough_storage=rough_storage
    )

    interactor.delete_rough_solution_to_question(
        question_id=question_id, rough_solution_id=rough_solution_id
    )

    response = HttpResponse(status=200)
    return response
