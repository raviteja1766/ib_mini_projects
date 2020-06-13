from content_management_portal.storages.rough_storage_implementation\
    import RoughSolutionStorageImplementation
import pytest
from freezegun import freeze_time
from content_management_portal.models import RoughSolution
from content_management_portal.constants.enums import CodeLanguageType


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_validate_update_rough_solution_given_valid_details_returns_ids(
        create_rough_solutions, update_rough_solutions_dtos):

    # Arrange
    question_id = 1
    rough_id = 1
    file_name = "java.py"
    language = CodeLanguageType.JAVA.value
    code = "java_language"
    rough_storage = RoughSolutionStorageImplementation()

    # Act
    rough_storage.update_rough_solutions(
        question_id=question_id,
        rough_solutions_dto=update_rough_solutions_dtos)

    # Assert
    rough_obj = RoughSolution.objects.get(id=rough_id)
    assert rough_obj.file_name == file_name
    assert rough_obj.language == language
    assert rough_obj.code == code
