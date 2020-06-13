import pytest
from freezegun import freeze_time
from content_management_portal.storages\
    .clean_solution_storage_implementation\
    import CleanSolutionStorageImplementation
from content_management_portal.models import PrefilledCode


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_delete_clean_solution_given_valid_deletes_clean_solution(
        create_clean_solutions):

    # Assert
    clean_solution_id = 1
    clean_solution_storage = CleanSolutionStorageImplementation()

    # Act
    clean_solution_storage\
        .delete_clean_solution(clean_solution_id=clean_solution_id)

    # Assert
    assert PrefilledCode.objects\
        .filter(id=clean_solution_id).exists() == False
