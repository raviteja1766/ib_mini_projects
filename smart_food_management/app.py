from django.apps import AppConfig


class SmartFoodManagementAppConfig(AppConfig):
    name = "smart_food_management"

    def ready(self):
        from smart_food_management import signals # pylint: disable=unused-variable
