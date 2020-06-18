from django.apps import AppConfig


class FormMasterAppConfig(AppConfig):
    name = "form_master"

    def ready(self):
        from form_master import signals # pylint: disable=unused-variable
