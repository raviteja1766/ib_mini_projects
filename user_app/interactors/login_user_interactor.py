from user_app.interactors.presenters.presenter_interface\
    import PresenterInterface
from user_app.interactors.storages.user_storage_interface\
    import UserStorageInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service\
    import OAuthUserAuthTokensService
from user_app.exceptions.exceptions import InvalidPassword, InvalidUsername


class LoginUserInteractor:

    def __init__(self, user_storage: UserStorageInterface,
                 oauth_storage: OAuth2SQLStorage,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.oauth_storage = oauth_storage
        self.presenter = presenter

    def login_user(self, username: str, password: str):

        try:
            self.user_storage.validate_username(username=username)
        except InvalidUsername:
            self.presenter.raise_exception_for_invalid_username()
            return
        try:
            user_id = self.user_storage.validate_password_to_user(
                username=username, password=password
            )
        except InvalidPassword:
            self.presenter.raise_exception_for_invalid_password()
            return
        oauth_user_token_service = OAuthUserAuthTokensService(
            self.oauth_storage)
        accestoken_dto = oauth_user_token_service.create_user_auth_tokens(
            user_id=user_id
        )
        return self.presenter.get_response_for_login_user(accestoken_dto)
