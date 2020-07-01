from django.apps import AppConfig


class UserAppAppConfig(AppConfig):
    name = "user_app"

    def ready(self):
        from user_app import signals # pylint: disable=unused-variable
