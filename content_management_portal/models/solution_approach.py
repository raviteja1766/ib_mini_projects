from django.db import models
from .user import User
from content_management_portal.constants.enums import DescriptionType
from .question import Question


class SolutionApproach(models.Model):
    title = models.CharField(max_length=120)
    description_content_type = models.CharField(
        max_length=100,choices=DescriptionType.get_list_of_tuples()
    )
    description_content = models.TextField()
    complexity_content_type = models.CharField(
        max_length=100,choices=DescriptionType.get_list_of_tuples()
    )
    complexity_content = models.TextField()
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
