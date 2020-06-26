import enum
from datetime import datetime
import factory, factory.django
from content_management_portal.models import *
from content_management_portal.constants.enums \
    import CodeLanguageType, DescriptionType


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
    username = factory.Sequence(lambda n: "username_%d" % n)
    password = factory.Sequence(lambda n: "password_%d" % n)


class QuestionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Question
    short_text = factory.Sequence(lambda n: "short_text_%d" % n)
    text_type = factory.Iterator(DescriptionType.get_list_of_values())
    description = factory.Sequence(lambda n: "description_%d" % n)
    user = factory.SubFactory(UserFactory)


class RoughSolutionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = RoughSolution
    file_name = factory.Sequence(lambda n: "file_name_%d" % n)
    language = factory.Iterator(CodeLanguageType.get_list_of_values())
    code = factory.Sequence(lambda n: "code_%d" % n)
    question = factory.SubFactory(QuestionFactory)
    user = factory.LazyAttribute(lambda obj: obj.question.user)


class CleanSolutionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = CleanSolution
    file_name = factory.Sequence(lambda n: "file_name_%d" % n)
    language = factory.Iterator(CodeLanguageType.get_list_of_values())
    code = factory.Sequence(lambda n: "code_%d" % n)
    question = factory.SubFactory(QuestionFactory)
    user = factory.LazyAttribute(lambda obj: obj.question.user)


class PrefilledCodeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PrefilledCode
    file_name = factory.Sequence(lambda n: "file_name_%d" % n)
    language = factory.Iterator(CodeLanguageType.get_list_of_values())
    code = factory.Sequence(lambda n: "code_%d" % n)
    question = factory.SubFactory(QuestionFactory)
    user = factory.LazyAttribute(lambda obj: obj.question.user)


class TestCaseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = TestCase
    input_text = factory.Sequence(lambda n: "input_text_%d" % n)
    output_text = factory.Sequence(lambda n: "output_text_%d" % n)
    score = factory.Sequence(lambda n: n)
    order_id = factory.Sequence(lambda n: n)
    question = factory.SubFactory(QuestionFactory)
    user = factory.LazyAttribute(lambda obj: obj.question.user)


class SolutionApproachFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = SolutionApproach

    title = factory.Sequence(lambda n: "title_%d" % n)
    description_content_type = \
        factory.Iterator(DescriptionType.get_list_of_values())
    description_content = \
        factory.Sequence(lambda n: "description_content_%d" % n)
    complexity_content_type = \
        factory.Iterator(DescriptionType.get_list_of_values())
    complexity_content = \
        factory.Sequence(lambda n: "complexity_content_%d" % n)
    question = factory.SubFactory(QuestionFactory)
    user = factory.LazyAttribute(lambda obj: obj.question.user)



class HintFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Hint
    title = factory.Sequence(lambda n: "title_%d" % n)
    content_type = factory.Iterator(DescriptionType.get_list_of_values())
    content = factory.Sequence(lambda n: "content_%d" % n)
    order_id = factory.Sequence(lambda n: n)
    question = factory.SubFactory(QuestionFactory)
    user = factory.LazyAttribute(lambda obj: obj.question.user)
