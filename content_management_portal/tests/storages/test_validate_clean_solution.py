import pytest
from freezegun import freeze_time
from content_management_portal.storages.clean_solution_storage_implementation\
    import CleanSolutionStorageImplementation


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_clean_solution_given_valid_clean_solution_and_returns_true(
        create_clean_solutions):

    # Arrange
    clean_solution_id = 1
    clean_solution_storage = CleanSolutionStorageImplementation()
    expected_response = True

    # Act
    actual_response = clean_solution_storage.validate_clean_solution(
        clean_solution_id=clean_solution_id
    )

    # Assert
    assert actual_response == expected_response

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_clean_solution_given_invalid_clean_solution_and_returns_false(
        create_clean_solutions):

    # Arrange
    clean_solution_id = 2
    clean_solution_storage = CleanSolutionStorageImplementation()
    expected_response = False

    # Act
    actual_response = clean_solution_storage.validate_clean_solution(
        clean_solution_id=clean_solution_id
    )

    # Assert
    assert actual_response == expected_response
