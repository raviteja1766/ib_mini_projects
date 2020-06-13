from content_management_portal.storages.rough_storage_implementation\
    import RoughSolutionStorageImplementation
import pytest
from freezegun import freeze_time
from content_management_portal.models import RoughSolution


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_delete_rough_solution_given_valid_details_returns_true(
        create_rough_solutions):

    # Arrange
    rough_solution_id = 1
    rough_storage = RoughSolutionStorageImplementation()
    expected_output = False

    # Act
    rough_storage.delete_rough_solution(
        rough_solution_id=rough_solution_id)

    # Assert
    assert RoughSolution.objects.filter(id=rough_solution_id).exists() ==\
        expected_output