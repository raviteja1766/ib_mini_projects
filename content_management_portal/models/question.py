from django.db import models
from content_management_portal.constants.enums import DescriptionType


class Question(models.Model):
    short_text = models.CharField(max_length=120)
    text_type = models.CharField(
        max_length=100,choices=DescriptionType.get_list_of_tuples()
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user_id = models.IntegerField()
