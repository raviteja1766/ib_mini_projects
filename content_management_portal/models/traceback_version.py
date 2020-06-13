from django.db import models
from .user import User
from content_management_portal.constants.enums import CodeLanguageType
from .question import Question
from content_management_portal.constants.enums import DescriptionType
from .rough_solution import RoughSolution


class UpdateVersionController(models.Model):

    changed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    changed_at = models.DateTimeField(auto_now=True)
    changed_question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True
    )
    changed_roughsolution = models.ForeignKey(
        RoughSolution, on_delete=models.CASCADE, null=True
    )
    changed_field = models.CharField(max_length=120)
    changed_data = models.TextField()


class CreateVersionController(models.Model):

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    created_question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )
    changed_roughsolution = models.ForeignKey(
        RoughSolution, on_delete=models.SET_NULL, null=True
    )


class DeleteVersionController(models.Model):

    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(auto_now=True)
    deleted_question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )
    deleted_roughsolution = models.ForeignKey(
        RoughSolution, on_delete=models.SET_NULL, null=True
    )
