from django.db import models
from .user import User
from content_management_portal.constants.enums import CodeLanguageType
from .question import Question


class CleanSolution(models.Model):
    file_name = models.CharField(max_length=120)
    language = models.CharField(
        max_length=100, choices=CodeLanguageType.get_list_of_tuples()
    )
    code = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
