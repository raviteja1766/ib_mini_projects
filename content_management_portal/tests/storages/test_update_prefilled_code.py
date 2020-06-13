from content_management_portal.storages\
    .prefilled_code_storage_implementation\
    import PrefilledCodeStorageImplementation
import pytest
from content_management_portal.models import PrefilledCode
from content_management_portal.constants.enums import CodeLanguageType


@pytest.mark.django_db
def test_validate_update_prefilled_code_given_valid_details_returns_ids(
        create_prefilled_codes, update_prefilled_codes_dto):

    # Arrange
    question_id = 1
    prefilled_id = 1
    file_name = "java.py"
    language = CodeLanguageType.JAVA.value
    code = "java_language"
    prefilled_storage = PrefilledCodeStorageImplementation()

    # Act
    prefilled_storage.update_prefilled_codes(
        question_id=question_id,
        prefilled_codes_dto=update_prefilled_codes_dto)

    # Assert
    prefilled_obj = PrefilledCode.objects.get(id=prefilled_id)
    assert prefilled_obj.file_name == file_name
    assert prefilled_obj.language == language
    assert prefilled_obj.code == code
