from django_swagger_utils.utils.test import CustomAPITestCase
from freezegun import freeze_time

from content_management_portal.factories.factories import (
    UserFactory, QuestionFactory, RoughSolutionFactory,
    CleanSolutionFactory, PrefilledCodeFactory, TestCaseFactory,
    SolutionApproachFactory, HintFactory
)
from content_management_portal.models import *


class CustomTestUtils(CustomAPITestCase):

    def reset_factory_sequence(self):
        UserFactory.reset_sequence(2)
        QuestionFactory.reset_sequence(1)
        RoughSolutionFactory.reset_sequence(1)
        CleanSolutionFactory.reset_sequence(1)
        PrefilledCodeFactory.reset_sequence(1)
        TestCaseFactory.reset_sequence(1)
        SolutionApproachFactory.reset_sequence(1)
        HintFactory.reset_sequence(1)

    def create_users(self):
        self.reset_factory_sequence()
        UserFactory()

    @freeze_time("2019-03-04")
    def create_questions(self):
        QuestionFactory.text_type.reset()
        users = list(User.objects.all())
        for user in users:
            QuestionFactory.create_batch(size=4, user=user)

    def create_rough_solutions(self):
        questions = list(Question.objects.filter(user_id=1))
        for question in questions:
            RoughSolutionFactory.create_batch(size=4, question=question)

    def create_clean_solutions(self):
        questions = list(Question.objects.filter(user_id=1))
        for question in questions:
            CleanSolutionFactory.create_batch(size=4, question=question)

    def create_prefilled_codes(self):
        questions = list(Question.objects.filter(user_id=1))
        for question in questions:
            PrefilledCodeFactory.create_batch(size=4, question=question)

    def create_tests(self):
        questions = list(Question.objects.filter(user_id=1))
        for question in questions:
            TestCaseFactory(question=question, score=10, order_id=1)
            TestCaseFactory(question=question, score=20, order_id=2)
            TestCaseFactory(question=question, score=30, order_id=3)
            TestCaseFactory(question=question, score=40, order_id=4)

    def create_solution_approach(self):
        questions = list(Question.objects.filter(user_id=1))
        for question in questions:
            SolutionApproachFactory(question=question)

    def create_hints(self):
        questions = list(Question.objects.filter(user_id=1))
        for question in questions:
            HintFactory(question=question, order_id=1)
            HintFactory(question=question, order_id=2)
            HintFactory(question=question, order_id=3)
            HintFactory(question=question, order_id=4)
