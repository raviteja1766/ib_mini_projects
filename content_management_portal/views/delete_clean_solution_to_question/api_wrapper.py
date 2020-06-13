from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.clean_solution_storage_implementation\
    import CleanSolutionStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .delete_clean_solution_interactor\
    import DeleteCleanSolutionInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = int(kwargs['question_id'])
    clean_solution_id = int(kwargs['clean_solution_id'])
    question_storage = QuestionStorageImplementation()
    clean_solution_storage = CleanSolutionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteCleanSolutionInteractor(
        question_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage
    )

    interactor.delete_clean_solution_to_question(
        question_id=question_id, clean_solution_id=clean_solution_id
    )
    response = HttpResponse(status=200)
    return response
