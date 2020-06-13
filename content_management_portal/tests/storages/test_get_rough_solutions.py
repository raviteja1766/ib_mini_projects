from content_management_portal.storages.rough_storage_implementation\
    import RoughSolutionStorageImplementation
import pytest
from freezegun import freeze_time
from content_management_portal.models import RoughSolution

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_rough_solution_given_valid_details_returns_details_dto(
        create_rough_solutions, rough_solutions_dtos):

    # Arrange
    question_id = 1
    rough_storage = RoughSolutionStorageImplementation()

    # Act
    expected_output = rough_storage\
        .get_rough_solutions_to_question(question_id=question_id)

    # Assert
    assert rough_solutions_dtos == expected_output
