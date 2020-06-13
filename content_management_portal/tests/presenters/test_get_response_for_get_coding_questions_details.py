from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors.storages.dtos\
    import CodingQuestionDto


def test_get_response_for_get_coding_questions_details_returns_details():

    # Arrange
    offset = 0
    limit = 1
    questions_count = 1
    coding_questions_dto = [
        CodingQuestionDto(
            question_id=1,
            short_text="short_text1",
            rough_solutions=True,
            test_cases=False,
            prefilled_code=False,
            solution_approach=False,
            clean_solution=False
        )
    ]

    expected_output = {
        "total_questions": 1,
        "offset": 0,
        "limit": 1,
        "questions_list": [{
            "question_id": 1,
            "statement": "short_text1",
            "rough_solution_status": True,
            "test_cases_status": False,
            "prefilled_code_status": False,
            "solution_approach_status": False,
            "clean_solution_status": False
        }]
    }
    presenter = PresenterImplementation()

    # Act
    presenter_response = presenter.get_response_for_get_coding_questions_details(
        offset=offset, limit=limit,
        questions_count=questions_count,
        coding_questions_dto=coding_questions_dto
    )

    # Assert
    assert presenter_response == expected_output
