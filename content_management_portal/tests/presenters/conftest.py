import pytest
import datetime
from content_management_portal.interactors.storages.dtos import (
    QuestionDto, RoughSolutionDto, TestCaseDto, PrefilledCodeDto,
    CleanSolutionDto, SolutionApproachDto, HintDto
)
from content_management_portal.constants.enums import (
    CodeLanguageType, DescriptionType
)


@pytest.fixture()
def question_dto():

    return QuestionDto(
        id=1,
        short_text="short_text1",
        text_type=DescriptionType.HTML.value,
        description="description1",
        created_at=datetime.datetime(2012, 1, 13),
        user_id=1
    )

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
def prefilled_codes_dto():

    return [
        PrefilledCodeDto(
            id=1, file_name="prime.py", user_id=1,
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


@pytest.fixture()
def question_complete_details_dto(
        question_dto, rough_solutions_dtos,
        test_case_dto, prefilled_codes_dto,
        solution_approach_dto, clean_solutions_dto,
        hint_dto
        ):

    return (
        question_dto, rough_solutions_dtos, [test_case_dto],
        prefilled_codes_dto, solution_approach_dto,
        clean_solutions_dto, [hint_dto]
    )


@pytest.fixture
def question_complete_details_dto_response(
        test_case_sub_dto_response,
        solution_approach_sub_dto_response,
        hint_dto_sub_response):

    return {
        "question_id": 1,
        "statement": {
            "short_text": "short_text1",
            "problem_description": {
                "content_type": DescriptionType.HTML.value,
                "content": "description1"
            }
        },
        "rough_solutions": [
            {
                "rough_solution_id": 1,
                "file_name": "prime.py",
                "language": CodeLanguageType.PYTHON.value,
                "solution_content": "code_language"
            }
        ],
        "test_cases": [test_case_sub_dto_response],
        "prefilled_codes": [
            {
                "prefilled_code_id": 1,
                "file_name": "prime.py",
                "language": CodeLanguageType.PYTHON.value,
                "solution_content": "code_language"
            }
        ],
        "solution_approach": solution_approach_sub_dto_response,
        "clean_solutions": [
            {
                "clean_solution_id": 1,
                "file_name": "prime.py",
                "language": CodeLanguageType.PYTHON.value,
                "solution_content": "code_language"
            }
        ],
        "hints": [hint_dto_sub_response]
    }

# -----------------TestcaseDto-------------------------------

@pytest.fixture()
def test_case_dto():

    return TestCaseDto(
        id=1, input_text="first input", output_text="first output", score=75,
        is_hidden=False, question_id=1, user_id=1, order_id=1
    )


@pytest.fixture()
def test_case_dto_response(test_case_sub_dto_response):

    return {
        "question_id": 1,
        "test_case": test_case_sub_dto_response
    }


@pytest.fixture()
def test_case_sub_dto_response():
    
    return {
        "test_case_id": 1,
        "input": "first input",
        "output": "first output",
        "score": 75,
        "test_case_number": 1,
        "is_hidden": False
    }

# -------------------------Solution-Approach------------------

@pytest.fixture()
def solution_approach_dto():

    return SolutionApproachDto(
        id = 1, title = "first approach",
        description_content_type = DescriptionType.HTML.value,
        description_content = "content_1",
        complexity_content_type = DescriptionType.HTML.value,
        complexity_content = "content_2",
        question_id = 1,
        user_id = 1
    )


@pytest.fixture()
def solution_approach_dto_response(solution_approach_sub_dto_response):

    return {
        "question_id": 1,
        "solution_approach": solution_approach_sub_dto_response
    }

@pytest.fixture()
def solution_approach_sub_dto_response():
    
    return {
        "solution_approach_id": 1,
        "title": "first approach",
        "description": {
          "content_type": DescriptionType.HTML.value,
          "content": "content_1"
        },
        "complexity_analysis": {
          "content_type": DescriptionType.HTML.value,
          "content": "content_2"
        }
    }

# -----------------Hint----------------------------------


@pytest.fixture()
def hint_dto():

    return HintDto(
        id=1, title="update_title_1", content_type=DescriptionType.HTML.value,
        content="update_content", order_id=1, question_id=1, user_id=1
    )

@pytest.fixture()
def hint_dto_response(hint_dto_sub_response):

    return {
        "question_id": 1,
        "hint": hint_dto_sub_response
    }

@pytest.fixture()
def hint_dto_sub_response():
    return {
        "hint_id": 1,
        "title": "update_title_1",
        "description": {
            "content_type": DescriptionType.HTML.value,
            "content": "update_content"
        },
        "hint_number": 1
    }