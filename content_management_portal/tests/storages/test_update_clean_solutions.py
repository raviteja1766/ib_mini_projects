from content_management_portal.storages\
    .clean_solution_storage_implementation\
    import CleanSolutionStorageImplementation
import pytest
from content_management_portal.models import CleanSolution
from content_management_portal.constants.enums import CodeLanguageType


@pytest.mark.django_db
def test_validate_update_clean_solution_given_valid_details_returns_ids(
        create_clean_solutions, update_clean_solutions_dto):

    # Arrange
    question_id = 1
    clean_solution_id = 1
    file_name = "java.py"
    language = CodeLanguageType.JAVA.value
    code = "java_language"
    prefilled_storage = CleanSolutionStorageImplementation()

    # Act
    prefilled_storage.update_clean_solutions(
        question_id=question_id,
        clean_solutions_dto=update_clean_solutions_dto)

    # Assert
    prefilled_obj = CleanSolution.objects.get(id=clean_solution_id)
    assert prefilled_obj.file_name == file_name
    assert prefilled_obj.language == language
    assert prefilled_obj.code == code
