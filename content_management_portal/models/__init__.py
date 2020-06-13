from .user import User
from .question import Question
from .rough_solution import RoughSolution
from .test_case import TestCase
from .prefilled_code import PrefilledCode
from .clean_solution import CleanSolution
from .solution_approach import SolutionApproach
from .hint import Hint


__all__ = [
    "User", "Question", "RoughSolution",
    "TestCase", "PrefilledCode", "CleanSolution",
    "SolutionApproach", "Hint"
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
