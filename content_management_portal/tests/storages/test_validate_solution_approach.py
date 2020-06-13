import pytest
from freezegun import freeze_time
from content_management_portal.storages\
    .solution_approach_storage_implementation\
    import SolutionApproachStorageImplementation
from content_management_portal.models import SolutionApproach


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_solution_approach_given_valid_solution_approach_and_returns_true(
        create_solution_approachs):

    # Arrange
    solution_approach_id = 1
    solution_approach_storage = SolutionApproachStorageImplementation()
    expected_response = True

    # Act
    actual_response = solution_approach_storage.validate_solution_approach(
        solution_approach_id=solution_approach_id
    )

    # Assert
    assert actual_response == expected_response

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_solution_approach_given_invalid_solution_approach_and_returns_false(
        create_solution_approachs):

    # Arrange
    solution_approach_id = 2
    solution_approach_storage = SolutionApproachStorageImplementation()
    expected_response = False

    # Act
    actual_response = solution_approach_storage.validate_solution_approach(
        solution_approach_id=solution_approach_id
    )

    # Assert
    assert actual_response == expected_response
