from django.apps import AppConfig


class ContentManagementPortalAppConfig(AppConfig):
    name = "content_management_portal"

    def ready(self):
        from content_management_portal import signals # pylint: disable=unused-variable
