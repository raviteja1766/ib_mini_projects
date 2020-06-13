import pytest
from freezegun import freeze_time
from content_management_portal.storages\
    .solution_approach_storage_implementation\
    import SolutionApproachStorageImplementation
from content_management_portal.models import SolutionApproach
from content_management_portal.constants.enums import DescriptionType

@pytest.mark.django_db
def test_create_solution_approach_given_solution_approach_dto_creates_and_returns_dto(
        create_questions, new_solution_approach_dto,
        created_solution_approach_dto):

    # Arrange
    solution_approach_id = 1
    title = "first approach"
    description_content_type = DescriptionType.HTML.value
    description_content = "content_1"
    complexity_content_type = DescriptionType.HTML.value
    complexity_content = "content_2"
    solution_approach_storage = SolutionApproachStorageImplementation()

    # Act
    storage_response = solution_approach_storage.create_solution_approach(
        solution_approach_dto=new_solution_approach_dto
    )

    # Assert
    solution_approach_obj = \
        SolutionApproach.objects.get(id=solution_approach_id)
    assert solution_approach_obj.title == title
    assert solution_approach_obj.description_content_type ==\
        description_content_type
    assert solution_approach_obj.description_content == description_content
    assert solution_approach_obj.complexity_content_type ==\
        complexity_content_type
    assert solution_approach_obj.complexity_content == complexity_content
    assert storage_response == created_solution_approach_dto
