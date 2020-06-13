from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from typing import Dict, List
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.interactors.storages.dtos\
    import CleanSolutionDto
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.clean_solution_storage_implementation\
    import CleanSolutionStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .create_update_clean_solutions_interactor\
    import CreateUpdateCleanSolutionsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = int(kwargs['question_id'])
    clean_solutions_dict = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    clean_solution_storage = CleanSolutionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateUpdateCleanSolutionsInteractor(
        question_storage=question_storage, presenter=presenter,
        clean_solution_storage=clean_solution_storage)
    clean_solutions_dto = _convert_clean_solution_dict_to_dto(
        user_id=user.id, question_id=question_id,
        clean_solutions_dict=clean_solutions_dict)
    interactor_response = interactor\
        .create_update_clean_solutions(question_id,clean_solutions_dto)

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response

def _convert_clean_solution_dict_to_dto(
        user_id: int, question_id: int, clean_solutions_dict: List[Dict]):
    
    return [
        CleanSolutionDto(
            id=clean_solution_dict.get('clean_solution_id'),
            file_name=clean_solution_dict['file_name'],
            language_type=clean_solution_dict['language'],
            text_code=clean_solution_dict['solution_content'],
            question_id=question_id, user_id=user_id
        ) for clean_solution_dict in clean_solutions_dict
    ]