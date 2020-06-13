import pytest
from content_management_portal.storages\
    .clean_solution_storage_implementation\
    import CleanSolutionStorageImplementation
from content_management_portal.models import CleanSolution


@pytest.mark.django_db
def test_get_clean_solution_ids_given_valid_details_returns_ids(
        create_clean_solutions):

    # Arrange
    clean_solution_ids = [1]
    clean_storage = CleanSolutionStorageImplementation()

    # Act
    db_clean_solution_ids = clean_storage.get_database_clean_solution_ids(
        clean_solution_ids=clean_solution_ids)

    # Assert
    assert db_clean_solution_ids == clean_solution_ids
