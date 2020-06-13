from django.db import models
from .user import User
from .question import Question
from content_management_portal.constants.enums import DescriptionType


class Hint(models.Model):
    title = models.CharField(max_length=120)
    content_type = models.CharField(
        max_length=100,choices=DescriptionType.get_list_of_tuples()
    )
    content = models.TextField() 
    order_id = models.IntegerField(default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
