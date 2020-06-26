from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from typing import Dict, List
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.interactors.storages.dtos\
    import RoughSolutionDto
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages.rough_storage_implementation\
    import RoughSolutionStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .create_update_rough_solutions_interactor\
    import CreateUpdateRoughSolutionsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = int(kwargs['question_id'])
    rough_solutions_dict = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    rough_storage = RoughSolutionStorageImplementation()
    presenter = PresenterImplementation()
    rough_solutions_dto = _convert_rough_solution_dict_to_dto(
        user_id=user.id, question_id=question_id,
        rough_solutions_dict=rough_solutions_dict
    )
    interactor = CreateUpdateRoughSolutionsInteractor(
        question_id=question_id, solutions_dto=rough_solutions_dto,
        question_storage=question_storage, rough_storage=rough_storage
    )
    interactor_response = interactor\
        .base_create_update_solutions_wrapper(presenter=presenter)

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response

def _convert_rough_solution_dict_to_dto(
        user_id: int, question_id: int, rough_solutions_dict: List[Dict]):

    return [
        RoughSolutionDto(
            id=rough_solution_dict.get('rough_solution_id'),
            file_name=rough_solution_dict['file_name'],
            language_type=rough_solution_dict['language'],
            text_code=rough_solution_dict['solution_content'],
            question_id=question_id,
            user_id=user_id
        ) for rough_solution_dict in rough_solutions_dict
    ]