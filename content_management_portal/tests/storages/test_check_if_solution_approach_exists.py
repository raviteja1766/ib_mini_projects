import pytest
from freezegun import freeze_time
from content_management_portal.storages\
    .solution_approach_storage_implementation\
    import SolutionApproachStorageImplementation

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_check_if_solution_approach_exists_given_question_returns_true(
        create_solution_approachs):

    # Assert
    expected_response = True
    question_id = 1
    solution_approach_storage = SolutionApproachStorageImplementation()

    # Act
    actual_response = solution_approach_storage\
        .check_if_solution_approach_exists(
            question_id=question_id
        )

    # Assert
    assert actual_response == expected_response


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_check_if_solution_approach_exists_given_question_returns_false(
        create_questions):

    # Assert
    expected_response = False
    question_id = 1
    solution_approach_storage = SolutionApproachStorageImplementation()

    # Act
    actual_response = solution_approach_storage\
        .check_if_solution_approach_exists(
            question_id=question_id
        )

    # Assert
    assert actual_response == expected_response