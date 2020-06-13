from common.dtos import Application


class OAuth2SQLStorage:
    """
    Configure the following setting variables in your base.py
    - DEFAULT_OAUTH_APPLICATION_NAME: OAuth Application Name (i.e your project name)
    - DEFAULT_OAUTH_CLIENT_ID: Client ID generated when creating an OAuth Application
    - DEFAULT_OAUTH_CLIENT_SECRET: Client Secret generated when creating an OAuth Application
    - DEFAULT_OAUTH_SCOPES: Default Oauth Scopes
    - DEFAULT_ACCESS_TOKEN_EXPIRY_IN_SECONDS: Default Oauth Token expiry (set this to 1000000000) for development purpose only.

    """

    def get_or_create_default_application(self, user_id):
        from oauth2_provider.models import Application
        from oauth2_provider.models import AbstractApplication
        from django.conf import settings

        is_created = False
        application_name = settings.DEFAULT_OAUTH_APPLICATION_NAME
        try:
            application = Application.objects.get(name=application_name)
        except Application.DoesNotExist:
            application = Application.objects.create(
                client_id=settings.DEFAULT_OAUTH_CLIENT_ID,
                user_id=user_id,
                client_type=AbstractApplication.CLIENT_CONFIDENTIAL,
                authorization_grant_type=AbstractApplication.GRANT_PASSWORD,
                client_secret=settings.DEFAULT_OAUTH_CLIENT_SECRET,
                name=application_name
            )
            is_created = True

        return self._convert_application_to_its_dto(application=application), \
               is_created

    def create_access_token(self, user_id, application_id, scopes,
                            expiry_in_seconds):
        import datetime
        from oauth2_provider.models import AccessToken

        access_token = self._generate_access_token()
        expires = datetime.datetime.now() + datetime.timedelta(
            seconds=expiry_in_seconds
        )
        access_token_object = AccessToken(
            user_id=user_id,
            token=access_token,
            application_id=application_id,
            expires=expires,
            scope=scopes
        )
        access_token_object.save()

        from common.dtos import AccessTokenDTO
        return AccessTokenDTO(
            access_token_id=access_token_object.id,
            token=access_token_object.token,
            expires=expires
        )

    def create_refresh_token(self, user_id, application_id, access_token_id):
        from oauth2_provider.models import RefreshToken

        refresh_token = self._generate_access_token()
        refresh_token_object = RefreshToken(
            user_id=user_id, token=refresh_token,
            application_id=application_id,
            access_token_id=access_token_id
        )
        refresh_token_object.save()

        from common.dtos import RefreshTokenDTO
        return RefreshTokenDTO(
            token=refresh_token_object.token,
            access_token=refresh_token_object.access_token,
            user_id=refresh_token_object.user_id,
            revoked=refresh_token_object.revoked
        )

    @staticmethod
    def _generate_access_token():
        import string
        import random
        from builtins import range

        size = 30
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def _convert_application_to_its_dto(application):

        return Application(application_id=application.id)
