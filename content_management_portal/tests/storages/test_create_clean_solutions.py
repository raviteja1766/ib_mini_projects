import pytest
from content_management_portal.storages\
    .clean_solution_storage_implementation\
    import CleanSolutionStorageImplementation
from content_management_portal.models import CleanSolution


@pytest.mark.django_db
def test_validate_create_clean_solution_given_valid_details_returns_ids(
        create_clean_solutions, new_clean_solutions_dto):

    # Arrange
    clean_solution_id = 1
    prefilled_storage = CleanSolutionStorageImplementation()

    # Act
    prefilled_storage.create_clean_solutions(
        clean_solutions_dto=new_clean_solutions_dto)

    # Assert
    assert CleanSolution.objects\
        .filter(id=clean_solution_id).exists() == True
