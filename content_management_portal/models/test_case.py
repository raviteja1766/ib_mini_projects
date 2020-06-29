from django.db import models
from .question import Question


class TestCase(models.Model):
    input_text = models.TextField()
    output_text = models.TextField()
    score = models.IntegerField()
    is_hidden = models.BooleanField(default=True)
    order_id = models.IntegerField(default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.IntegerField()
