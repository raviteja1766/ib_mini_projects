from django.apps import AppConfig


class GyaanAppConfig(AppConfig):
    name = "gyaan"

    def ready(self):
        from gyaan import signals # pylint: disable=unused-variable
