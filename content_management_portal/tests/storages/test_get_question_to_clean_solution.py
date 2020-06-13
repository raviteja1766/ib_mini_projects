import pytest
from freezegun import freeze_time
from content_management_portal.storages.clean_solution_storage_implementation\
    import CleanSolutionStorageImplementation

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_question_to_clean_solution_given_clean_solution_returns_question_id(
        create_clean_solutions):

    # Assert
    clean_solution_id = 1
    question_id = 1
    clean_solution_storage = CleanSolutionStorageImplementation()

    # Act
    response_id = clean_solution_storage.get_question_to_clean_solution(
        clean_solution_id=clean_solution_id
    )

    # Assert
    assert response_id == question_id