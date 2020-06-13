import pytest
from freezegun import freeze_time
from content_management_portal.storages\
    .solution_approach_storage_implementation\
    import SolutionApproachStorageImplementation

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_question_to_solution_approach_given_solution_approach_returns_question_id(
        create_solution_approachs):

    # Assert
    solution_approach_id = 1
    question_id = 1
    solution_approach_storage = SolutionApproachStorageImplementation()

    # Act
    response_id = solution_approach_storage\
        .get_question_to_solution_approach(
            solution_approach_id=solution_approach_id
        )

    # Assert
    assert response_id == question_id