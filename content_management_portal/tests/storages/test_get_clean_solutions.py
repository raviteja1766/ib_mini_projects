import pytest
from content_management_portal.storages\
    .clean_solution_storage_implementation\
    import CleanSolutionStorageImplementation
from content_management_portal.models import CleanSolution


@pytest.mark.django_db
def test_validate_get_clean_solutions_given_valid_details_returns_details(
        create_clean_solutions, clean_solutions_dto):

    # Arrange
    question_id = 1
    clean_storage = CleanSolutionStorageImplementation()

    # Act
    clean_storage_response = clean_storage.get_clean_solutions_to_question(
        question_id=question_id
    )

    # Assert
    assert clean_storage_response == clean_solutions_dto
