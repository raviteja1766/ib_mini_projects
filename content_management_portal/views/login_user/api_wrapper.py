from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from django.http import HttpResponse
from content_management_portal.storages.user_storage_implementation\
    import UserStorageImplementation

from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors.login_user_interactor\
    import LoginUserInteractor
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_details_dict = kwargs['request_data']
    username = user_details_dict["username"]
    password = user_details_dict["password"]
    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    interactor = LoginUserInteractor(
        user_storage=user_storage, presenter=presenter,
        oauth_storage=oauth_storage
    )

    interactor_response = interactor.login_user(
        username=username,password=password)

    data = json.dumps(interactor_response)
    response = HttpResponse(data, status=200)
    return response