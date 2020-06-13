from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.test_case_storage_implementation\
    import TestCaseStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .delete_test_case_interactor\
    import DeleteTestCaseInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = int(kwargs['question_id'])
    test_case_id = int(kwargs['test_case_id'])
    question_storage = QuestionStorageImplementation()
    test_case_storage = TestCaseStorageImplementation()
    presenter = PresenterImplementation()
    interactor = DeleteTestCaseInteractor(
        question_storage=question_storage, presenter=presenter,
        test_case_storage=test_case_storage
    )

    interactor.delete_test_case_to_question(
        question_id=question_id, test_case_id=test_case_id
    )
    response = HttpResponse(status=200)
    return response
