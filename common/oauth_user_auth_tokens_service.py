from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage


class OAuthUserAuthTokensService:
    """
    Configure the following setting variables in your base.py
    - DEFAULT_OAUTH_APPLICATION_NAME: OAuth Application Name (i.e your project name)
    - DEFAULT_OAUTH_CLIENT_ID: Client ID generated when creating an OAuth Application
    - DEFAULT_OAUTH_CLIENT_SECRET: Client Secret generated when creating an OAuth Application
    - DEFAULT_OAUTH_SCOPES: Default Oauth Scopes
    - DEFAULT_ACCESS_TOKEN_EXPIRY_IN_SECONDS: Default Oauth Token expiry (set this to 1000000000) for development purpose only.

    """
    def __init__(self, oauth2_storage: OAuth2SQLStorage):
        self.oauth2_storage = oauth2_storage

    def create_user_auth_tokens(self, user_id):
        from django.conf import settings

        application, _ = self.oauth2_storage.get_or_create_default_application(
            user_id=user_id
        )

        access_token_obj = self.oauth2_storage.create_access_token(
            user_id=user_id,
            application_id=application.application_id,
            scopes=settings.DEFAULT_OAUTH_SCOPES,
            expiry_in_seconds=settings.DEFAULT_ACCESS_TOKEN_EXPIRY_IN_SECONDS
        )

        refresh_token_obj = self.oauth2_storage.create_refresh_token(
            user_id=user_id,
            application_id=application.application_id,
            access_token_id=access_token_obj.access_token_id
        )

        return UserAuthTokensDTO(
            user_id=user_id,
            access_token=access_token_obj.token,
            refresh_token=refresh_token_obj.token,
            expires_in=access_token_obj.expires
        )
