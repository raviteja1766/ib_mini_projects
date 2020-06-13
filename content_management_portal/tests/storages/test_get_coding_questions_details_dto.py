from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
from content_management_portal.interactors.storages.dtos\
    import CodingQuestionDto
import pytest
from freezegun import freeze_time


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_coding_questions_details_dto_returns_complete_coding_details(
        create_rough_solutions):

    # Arrange
    offset = 1
    limit = 1
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

    question_storage = QuestionStorageImplementation()

    # Act
    actual_dto_response = question_storage.get_coding_questions_details_dto(
        offset=offset, limit=limit
    )

    # Assert
    assert actual_dto_response == coding_questions_dto
