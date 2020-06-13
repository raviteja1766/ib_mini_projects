import pytest
from freezegun import freeze_time
from content_management_portal.storages\
    .solution_approach_storage_implementation\
    import SolutionApproachStorageImplementation
from content_management_portal.models import SolutionApproach
from content_management_portal.constants.enums import DescriptionType


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_solution_approach_given_solution_approach_dto_updates_and_returns_dto(
        update_solution_approach_dto, create_solution_approachs):

    # Arrange
    solution_approach_id = 1
    title = "updated approach"
    description_content_type = DescriptionType.HTML.value
    description_content = "updated content 1"
    complexity_content_type = DescriptionType.HTML.value
    complexity_content = "updated content 2"
    solution_approach_storage = SolutionApproachStorageImplementation()

    # Act
    storage_response = solution_approach_storage.update_solution_approach(
        solution_approach_dto=update_solution_approach_dto
    )

    # Assert
    solution_approach_obj = SolutionApproach.objects\
        .get(id=solution_approach_id)
    assert solution_approach_obj.title == title
    assert solution_approach_obj.description_content_type ==\
        description_content_type
    assert solution_approach_obj.description_content == description_content
    assert solution_approach_obj.complexity_content == complexity_content
    assert solution_approach_obj.complexity_content_type ==\
        complexity_content_type
    assert storage_response == update_solution_approach_dto

