import pytest
from datetime import datetime
from freezegun import freeze_time
from content_management_portal.models import (
    User, Question, RoughSolution, TestCase, PrefilledCode,
    CleanSolution, SolutionApproach, Hint
)
from content_management_portal.interactors.storages.dtos import *
from content_management_portal.constants.enums import (
    DescriptionType, CodeLanguageType
)


@pytest.fixture()
def create_users():

    users_list = [
        {
            'username': "username1",
            'password': "Mdjsfs@713"
        },
        {
            'username': "username2",
            'password': "Hksu@761"
        }
    ]
    user_instances_list = []
    users_password_dict = {}
    for user in users_list:
        users_password_dict[user['username']] = user['password']
        user_instances_list.append(
            User(username=user['username'])
        )

    User.objects.bulk_create(user_instances_list)
    user_objs = list(User.objects.all())
    for user in user_objs:
        password = users_password_dict[user.username]
        user.set_password(password)
    User.objects.bulk_update(user_objs, ['password'])

@pytest.fixture()
@freeze_time("2012-01-13")
def create_questions(create_users):

    Question.objects.bulk_create([
        Question(
            short_text="short_text1", text_type="HTML",
            description="description1", user_id=1
        )
    ])


@pytest.fixture()
@freeze_time("2012-01-13")
def create_rough_solutions(create_questions):

    RoughSolution.objects.bulk_create([
        RoughSolution(
            file_name="prime.py", language=CodeLanguageType.PYTHON.value,
            code="code_language", question_id=1, user_id=1
        )
    ])

@pytest.fixture()
@freeze_time("2012-01-13")
def create_test_cases(create_questions):

    TestCase.objects.bulk_create([
        TestCase(
            input_text="first input", output_text="first output", score=75,
            is_hidden=False, question_id=1, user_id=1, order_id=1
        )
    ])

@pytest.fixture()
@freeze_time("2012-01-13")
def create_prefilled_codes(create_questions):

    PrefilledCode.objects.bulk_create([
        PrefilledCode(
            file_name="prime.py", language=CodeLanguageType.PYTHON.value,
            code="code_language", question_id=1, user_id=1
        )
    ])

@pytest.fixture()
@freeze_time("2012-01-13")
def create_clean_solutions(create_questions):

    CleanSolution.objects.bulk_create([
        CleanSolution(
            file_name="prime.py", language=CodeLanguageType.PYTHON.value,
            code="code_language", question_id=1, user_id=1
        )
    ])

@pytest.fixture()
@freeze_time("2012-01-13")
def create_solution_approachs(create_questions):

    SolutionApproach.objects.bulk_create([
        SolutionApproach(
            title="first approach",
            description_content_type=DescriptionType.HTML.value,
            description_content="content_1",
            complexity_content_type=DescriptionType.HTML.value,
            complexity_content="content_2",
            question_id=1,
            user_id=1
        )
    ])

@pytest.fixture()
@freeze_time("2012-01-13")
def create_hints(create_questions):

    Hint.objects.bulk_create([
        Hint(
            id=None, title="title_1", content_type=DescriptionType.HTML.value,
            content="content", order_id=1, question_id=1, user_id=1
        )
    ])


# -------------------Rough-solutions---------------------

@pytest.fixture()
def rough_solutions_dtos():

    return [
        RoughSolutionDto(
            id=1, file_name="prime.py",
            language_type=CodeLanguageType.PYTHON.value,
            text_code="code_language", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def update_rough_solutions_dtos():

    return [
        RoughSolutionDto(
            id=1, file_name="java.py",
            language_type=CodeLanguageType.JAVA.value,
            text_code="java_language", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def new_rough_solutions_dto():
    return [
        RoughSolutionDto(
            id=None, file_name="prime.py",
            language_type=CodeLanguageType.PYTHON.value,
            text_code="code_language", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def question_dto():

    return QuestionDto(
        id=1,
        short_text="short_text1",
        text_type="HTML",
        description="description1",
        created_at=datetime.datetime(2012, 1, 13),
        user_id=1
    )


@pytest.fixture()
def update_question_dto():

    return QuestionDto(
        id=1,
        short_text="short_text2",
        text_type="HTML",
        description="description2",
        created_at=datetime.datetime(2012, 1, 13),
        user_id=1
    )

# ------------Get Question ----------------------

@pytest.fixture()
def test_cases_dto():

    return [
        TestCaseDto(
            id=1, input_text="first input", output_text="first output", score=75,
            is_hidden=False, question_id=1, user_id=1, order_id=1
        )
    ]

@pytest.fixture()
def hints_dto():
    
    return [
        HintDto(
            id=1, title="title_1", content_type=DescriptionType.HTML.value,
            content="content", order_id=1, question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def solution_approach_dto():
    
    return SolutionApproachDto(
        id=1,
        title="first approach",
        description_content_type=DescriptionType.HTML.value,
        description_content="content_1",
        complexity_content_type=DescriptionType.HTML.value,
        complexity_content="content_2",
        question_id=1,
        user_id=1
    )

@pytest.fixture()
def question_complete_details_dto(
        question_dto, rough_solutions_dtos, test_cases_dto,
        prefilled_codes_dto, clean_solutions_dto, hints_dto,
        solution_approach_dto
        ):

    return (
        question_dto, rough_solutions_dtos, test_cases_dto,
        prefilled_codes_dto, solution_approach_dto,
        clean_solutions_dto, hints_dto
    )

# --------------Create-Update-Test-Case-----------------------

@pytest.fixture()
def new_test_case_dto():

    return TestCaseDto(
        id=None, input_text="", output_text="output", score=75,
        is_hidden=True, question_id=1, user_id=1, order_id=1
    )

@pytest.fixture()
def created_test_case_dto():

    return TestCaseDto(
        id=1, input_text="", output_text="output", score=75,
        is_hidden=True, question_id=1, user_id=1,order_id=1
    )


@pytest.fixture()
def update_test_case_dto():

    return TestCaseDto(
        id=1, input_text="first input", output_text="first output", score=75,
        is_hidden=False, question_id=1, user_id=1,order_id=1
    )


# -----------------Prefilled-code---------------------------

@pytest.fixture()
def update_prefilled_codes_dto():

    return [
        PrefilledCodeDto(
            id=1, file_name="java.py",
            language_type=CodeLanguageType.JAVA.value,
            text_code="java_language", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def new_prefilled_codes_dto():
    return [
        PrefilledCodeDto(
            id=None, file_name="prime.py", user_id=1,
            language_type=CodeLanguageType.PYTHON.value,
            text_code="code_language", question_id=1
        )
    ]


@pytest.fixture()
def prefilled_codes_dto():

    return [
        PrefilledCodeDto(
            id=1, file_name="prime.py", user_id=1,
            language_type=CodeLanguageType.PYTHON.value,
            text_code="code_language", question_id=1
        )
    ]

# -------------------Clean-Solutions----------------------

@pytest.fixture()
def update_clean_solutions_dto():

    return [
        CleanSolutionDto(
            id=1, file_name="java.py",
            language_type=CodeLanguageType.JAVA.value,
            text_code="java_language", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def new_clean_solutions_dto():
    return [
        CleanSolutionDto(
            id=None, file_name="prime.py", user_id=1,
            language_type=CodeLanguageType.PYTHON.value,
            text_code="code_language", question_id=1
        )
    ]


@pytest.fixture()
def clean_solutions_dto():

    return [
        CleanSolutionDto(
            id=1, file_name="prime.py", user_id=1,
            language_type=CodeLanguageType.PYTHON.value,
            text_code="code_language", question_id=1
        )
    ]


# -------------------Solution-Approaches----------------------

@pytest.fixture()
def new_solution_approach_dto():

    return SolutionApproachDto(
        id=None, title="first approach",
        description_content_type=DescriptionType.HTML.value,
        description_content="content_1",
        complexity_content_type=DescriptionType.HTML.value,
        complexity_content="content_2",
        question_id=1,
        user_id=1
    )

@pytest.fixture()
def created_solution_approach_dto():

    return SolutionApproachDto(
        id=1, title="first approach",
        description_content_type=DescriptionType.HTML.value,
        description_content="content_1",
        complexity_content_type=DescriptionType.HTML.value,
        complexity_content="content_2",
        question_id=1,
        user_id=1
    )


@pytest.fixture()
def update_solution_approach_dto():

    return SolutionApproachDto(
        id=1, title="updated approach",
        description_content_type=DescriptionType.HTML.value,
        description_content="updated content 1",
        complexity_content_type=DescriptionType.HTML.value,
        complexity_content="updated content 2",
        question_id=1, user_id=1
    )

# ---------------Hints-------------------------------------


@pytest.fixture()
def new_hint_dto():

    return HintDto(
        id=None, title="title_1", content_type=DescriptionType.HTML.value,
        content="content", order_id=1, question_id=1, user_id=1
    )

@pytest.fixture()
def created_hint_dto():

    return HintDto(
        id=1, title="title_1", content_type=DescriptionType.HTML.value,
        content="content", order_id=1, question_id=1, user_id=1
    )


@pytest.fixture()
def update_hint_dto():

    return HintDto(
        id=1, title="update_title_1", content_type=DescriptionType.HTML.value,
        content="update_content", order_id=1, question_id=1, user_id=1
    )

# -------------------------TestCaseSwap---------------------

@pytest.fixture()
def update_test_cases_swap_dto():

    return [TestCaseSwapDto(id=1, order_id=3)]


# -----------------HintSwap------------------------------


@pytest.fixture()
def update_hints_swap_dto():

    return [HintSwapDto(id=1, order_id=3)]
