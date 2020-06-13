from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from typing import Dict
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.interactors.storages.dtos\
    import SolutionApproachDto
from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.storages\
    .solution_approach_storage_implementation\
    import SolutionApproachStorageImplementation
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors\
    .create_update_solution_approach_interactor\
    import CreateUpdateSolutionApproachInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    question_id = int(kwargs['question_id'])
    solution_dict = kwargs['request_data']
    question_storage = QuestionStorageImplementation()
    solution_approach_storage = SolutionApproachStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateUpdateSolutionApproachInteractor(
        question_storage=question_storage, presenter=presenter,
        solution_approach_storage=solution_approach_storage)
    solution_approach_dto = _convert_solution_dict_to_dto(
        user_id=user.id, question_id=question_id,
        solution_dict=solution_dict)
    interactor_response = interactor\
        .create_update_solution_approach(
            solution_approach_dto=solution_approach_dto
        )
    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=201)
    return response

def _convert_solution_dict_to_dto(
        user_id: int, question_id: int, solution_dict: Dict):
    
    return SolutionApproachDto(
        id=solution_dict.get('solution_approach_id'),
        title=solution_dict['title'],
        description_content_type=\
            solution_dict['description']['content_type'],
        description_content=solution_dict['description']['content'],
        complexity_content_type=\
            solution_dict['complexity_analysis']['content_type'],
        complexity_content=solution_dict['complexity_analysis']['content'],
        question_id=question_id,
        user_id=user_id
    )