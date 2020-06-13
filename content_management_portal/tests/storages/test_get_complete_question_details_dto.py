from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
import pytest
from freezegun import freeze_time


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_complete_question_details_given_valid_details_returns_details(
        create_rough_solutions,create_test_cases,
        create_prefilled_codes, create_clean_solutions,
        create_solution_approachs, create_hints, 
        question_complete_details_dto):

    # Arrange
    (
        question_dto, rough_solutions_dto, test_cases_dto,
        prefilled_codes_dto, solution_approach_dto,
        clean_solutions_dto, hints_dto
    ) = question_complete_details_dto
    question_id = 1
    question_storage = QuestionStorageImplementation()

    # Act
    (
        actual_question_dto, actual_rough_solutions_dto,
        actual_test_cases_dto, actual_prefilled_codes_dto,
        actual_solution_approach_dto,
        actual_clean_solutions_dto, actual_hints_dto
    ) = question_storage.get_complete_question_details_dto(
        question_id=question_id)

    # Assert
    assert question_dto == actual_question_dto
    assert rough_solutions_dto == actual_rough_solutions_dto
    assert test_cases_dto == actual_test_cases_dto
    assert prefilled_codes_dto == actual_prefilled_codes_dto
    assert solution_approach_dto == actual_solution_approach_dto
    assert clean_solutions_dto == actual_clean_solutions_dto
    assert hints_dto == actual_hints_dto
