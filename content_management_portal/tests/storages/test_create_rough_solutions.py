import pytest
from freezegun import freeze_time
from content_management_portal.storages.rough_storage_implementation\
    import RoughSolutionStorageImplementation
from content_management_portal.models import RoughSolution


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_update_rough_solution_given_valid_details_returns_ids(
        create_rough_solutions, new_rough_solutions_dto):

    # Arrange
    rough_id = 1
    rough_storage = RoughSolutionStorageImplementation()

    # Act
    rough_storage.create_rough_solutions(
        rough_solutions_dto=new_rough_solutions_dto)

    # Assert
    assert RoughSolution.objects.filter(id=rough_id).exists() == True
