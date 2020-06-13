import pytest
import datetime
from content_management_portal.constants.enums\
    import DescriptionType, CodeLanguageType
from content_management_portal.interactors.storages.dtos\
    import (
        QuestionDto, RoughSolutionDto, CodingQuestionDto,
        TestCaseDto, PrefilledCodeDto, CleanSolutionDto,
        SolutionApproachDto, HintDto, TestCaseSwapDto, HintSwapDto
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

# ------------Rough-solutions-dto----------------------

@pytest.fixture()
def rough_solutions_dict():
    rough_solutions_dict = [
        {
            "rough_solution_id": 1,
            "file_name": "prime.py",
            "language": CodeLanguageType.PYTHON.value,
            "solution_content": "text code for python"
        },
        {
            "rough_solution_id": None,
            "file_name": "java.py",
            "language": CodeLanguageType.JAVA.value,
            "solution_content": "text code for java"
        }
    ]
    return rough_solutions_dict


@pytest.fixture()
def rough_solutions_dto():

    return [
        RoughSolutionDto(
            id=1, file_name="prime.py", language_type="PYTHON",
            text_code="text code for python", question_id=1, user_id=1
        ),
        RoughSolutionDto(
            id=2, file_name="java.py", language_type="JAVA",
            text_code="text code for java", question_id=1, user_id=1
        )
    ]


@pytest.fixture()
def new_rough_solutions_dto():
    return [
        RoughSolutionDto(
            id=None, file_name="java.py", language_type="JAVA",
            text_code="text code for java", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def update_rough_solutions_dto():
    
    return [
        RoughSolutionDto(
            id=1, file_name="prime.py", language_type="PYTHON",
            text_code="text code for python", question_id=1, user_id=1
        )
    ]


@pytest.fixture()
def rough_solutions_dto_response():

    rough_solutions_dict = [
        {
            "rough_solution_id": 1,
            "header_text": {
                "file_name": "prime.py",
                "language_type": "PYTHON"
            },
            "text_code": "code_language"
        },
        {
            "rough_solution_id": 2,
            "header_text": {
                "file_name": "java.py",
                "language_type": "JAVA"
            },
            "text_code": "text code for java"
        }
    ]
    return rough_solutions_dict

# ---------------Coding questions------------------


@pytest.fixture()
def coding_questions_dto():
    return [
        CodingQuestionDto(
            question_id=1, short_text="short_text1",
            rough_solutions=True, test_cases=False,
            prefilled_code=True, solution_approach=False,
            clean_solution=True
        )
    ]

@pytest.fixture()
def coding_questions_complete_details():

    return {
        "total_questions": 1,
        "offset": 0,
        "limit": 1,
        "questions_details": [{
            "question_id": 1,
            "statement": "short_text1",
            "rough_solution_status": True,
            "test_cases_status": False,
            "prefilled_code_status": False,
            "solution_approach_status": False,
            "clean_solution_status": False
        }]
    }

# ------------------Question Complete Details -----------------


@pytest.fixture()
def question_complete_details_dto(
        question_dto, rough_solutions_dto, update_test_case_dto,
        update_prefilled_codes_dto, update_solution_approach_dto,
        update_clean_solutions_dto, update_hint_dto
        ):

    return (
        question_dto, rough_solutions_dto, update_test_case_dto,
        update_prefilled_codes_dto, update_solution_approach_dto,
        update_clean_solutions_dto, update_hint_dto
    )

@pytest.fixture()
def question_complete_details_dto_response(rough_solutions_dto_response):

    return {
        "question_id": 0,
        "problem_statement": {
            "short_text": "short_text1",
            "problem_description": {
                "text_type": DescriptionType.HTML.value,
                "text_description": "description1"
            }
        },
        "rough_solutions": rough_solutions_dto_response
    }

# ----------------Test cases------------------------

@pytest.fixture()
def update_test_case_dto():

    return TestCaseDto(
        id=1, input_text="first input", output_text="first output", score=75,
        is_hidden=False, question_id=1, user_id=1, order_id = 1
    )

@pytest.fixture()
def update_test_case_dict():

    return {
        "test_case_id": 1,
        "input_text": "first input",
        "output_text": "first output",
        "score": 75,
        "is_hidden": False
    }


@pytest.fixture()
def new_test_case_dto():

    return TestCaseDto(
        id=None, input_text="", output_text="output", score=75,
        is_hidden=True, question_id=1, user_id=1, order_id = 2
    )

@pytest.fixture()
def new_test_case_dict():

    return {
        "test_case_id": 1,
        "input_text": "",
        "output_text": "output",
        "score": 75,
        "is_hidden": True
    }

# ------------Prefilled-codes-----------------------------


@pytest.fixture()
def prefilled_codes_dto():

    return [
        PrefilledCodeDto(
            id=1, file_name="prime.py", language_type="PYTHON",
            text_code="text code for python", question_id=1, user_id=1
        ),
        PrefilledCodeDto(
            id=None, file_name="java.py", language_type="JAVA",
            text_code="text code for java", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def new_prefilled_codes_dto():
    return [
        PrefilledCodeDto(
            id=None, file_name="java.py", language_type="JAVA",
            text_code="text code for java", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def update_prefilled_codes_dto():
    return [
        PrefilledCodeDto(
            id=1, file_name="prime.py", language_type="PYTHON",
            text_code="text code for python", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def prefilled_codes_dto_response():

    prefilled_codes_dict = [
        {
            "prefilled_code_id": 1,
            "header_text": {
                "file_name": "prime.py",
                "language_type": "PYTHON"
            },
            "text_code": "text code for python"
        },
        {
            "prefilled_code_id": 2,
            "header_text": {
                "file_name": "java.py",
                "language_type": "JAVA"
            },
            "text_code": "text code for java"
        }
    ]
    return prefilled_codes_dict

# ---------------Clean-Solution--------------------------------


@pytest.fixture()
def clean_solutions_dto():

    return [
        CleanSolutionDto(
            id=1, file_name="prime.py", language_type="PYTHON",
            text_code="text code for python", question_id=1, user_id=1
        ),
        CleanSolutionDto(
            id=None, file_name="java.py", language_type="JAVA",
            text_code="text code for java", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def new_clean_solutions_dto():
    return [
        CleanSolutionDto(
            id=None, file_name="java.py", language_type="JAVA",
            text_code="text code for java", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def update_clean_solutions_dto():
    return [
        CleanSolutionDto(
            id=1, file_name="prime.py", language_type="PYTHON",
            text_code="text code for python", question_id=1, user_id=1
        )
    ]

@pytest.fixture()
def clean_solutions_dto_response():

    clean_solutions_dict = [
        {
            "clean_solution_id": 1,
            "header_text": {
                "file_name": "prime.py",
                "language_type": "PYTHON"
            },
            "text_code": "text code for python"
        },
        {
            "clean_solution_id": 2,
            "header_text": {
                "file_name": "java.py",
                "language_type": "JAVA"
            },
            "text_code": "text code for java"
        }
    ]
    return clean_solutions_dict

# ---------------------Solution-Approach-----------------------


@pytest.fixture()
def update_solution_approach_dto():

    return SolutionApproachDto(
        id=1, title="updated approach",
        description_content_type=DescriptionType.HTML.value,
        description_content="updated content 1",
        complexity_content_type=DescriptionType.HTML.value,
        complexity_content="updated content 2",
        question_id=1,
        user_id=1
    )

@pytest.fixture()
def update_solution_approach_dict():

    return {
        "solution_approach_id": 0,
        "title": "string",
        "description": {
          "content_type": "HTML",
          "content": "string"
        },
        "complexity_analysis": {
          "content_type": "HTML",
          "content": "string"
        }
    }


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
def new_solution_approach_dict():

    return {
        "solution_approach_id": 0,
        "title": "string",
        "description": {
          "content_type": "HTML",
          "content": "string"
        },
        "complexity_analysis": {
          "content_type": "HTML",
          "content": "string"
        }
    }


# ---------------------------Hints--------------------------


@pytest.fixture()
def update_hint_dto():

    return HintDto(
        id=1, title="update_title_1", content_type=DescriptionType.HTML.value,
        content="update_content", order_id=1, question_id=1, user_id=1
    )

@pytest.fixture()
def update_hint_dict():

    return {
        "title": "string",
        "description": {
            "content_type": "HTML",
            "content": "string"
        },
        "order": 0
    }


@pytest.fixture()
def new_hint_dto():

    return HintDto(
        id=None, title="title_1", content_type=DescriptionType.HTML.value,
        content="content", order_id=None, question_id=1, user_id=1
    )

@pytest.fixture()
def new_hint_dict():

    return {
        "title": "string",
        "description": {
            "content_type": "HTML",
            "content": "string"
        },
        "order": 0
    }


# -------------------TestcasesSwap------------------------------

@pytest.fixture()
def test_cases_swap_dto():
    
    return [
        TestCaseSwapDto(id=2, order_id=5),
        TestCaseSwapDto(id=5, order_id=2)
    ]


# ----------------HintSwap------------------------------------

@pytest.fixture()
def hints_swap_dto():
    
    return [
        HintSwapDto(id=2, order_id=5),
        HintSwapDto(id=5, order_id=2)
    ]
