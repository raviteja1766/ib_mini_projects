from content_management_portal.storages.rough_storage_implementation\
    import RoughSolutionStorageImplementation
import pytest
from freezegun import freeze_time


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_rough_solution_given_valid_details_returns_true(
        create_rough_solutions):

    # Arrange
    rough_solution_id = 1
    rough_storage = RoughSolutionStorageImplementation()
    expected_output = True

    # Act
    actual_output = rough_storage.validate_rough_solution_id(
        rough_solution_id=rough_solution_id)

    # Assert
    assert actual_output == expected_output


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_rough_solution_given_invalid_details_returns_false(
        create_rough_solutions):

    # Arrange
    rough_solution_id = 2
    rough_storage = RoughSolutionStorageImplementation()
    expected_output = False

    # Act
    actual_output = rough_storage.validate_rough_solution_id(
        rough_solution_id=rough_solution_id)

    # Assert
    assert actual_output == expected_output
