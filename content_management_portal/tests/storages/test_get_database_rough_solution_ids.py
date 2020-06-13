from content_management_portal.storages.rough_storage_implementation\
    import RoughSolutionStorageImplementation
import pytest
from freezegun import freeze_time


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_update_rough_solution_given_valid_details_returns_ids(
        create_rough_solutions):

    # Arrange
    rough_solution_ids = [1]
    rough_storage = RoughSolutionStorageImplementation()
    expected_output = [1]

    # Act
    actual_output = rough_storage.get_database_rough_solution_ids(
        rough_solution_ids=rough_solution_ids)

    # Assert
    assert actual_output == expected_output
