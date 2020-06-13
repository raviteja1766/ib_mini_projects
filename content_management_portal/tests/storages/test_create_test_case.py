import pytest
from freezegun import freeze_time
from content_management_portal.storages.test_case_storage_implementation\
    import TestCaseStorageImplementation
from content_management_portal.models import TestCase

@pytest.mark.django_db
def test_create_test_case_given_test_case_dto_creates_and_returns_dto(
        create_questions, new_test_case_dto, created_test_case_dto):

    # Arrange
    test_case_id = 1
    input_text=""
    output_text="output"
    score=75
    is_hidden=True
    test_case_storage = TestCaseStorageImplementation()

    # Act
    storage_response = test_case_storage.create_test_case(
        test_case_dto=new_test_case_dto
    )

    # Assert
    test_case_obj = TestCase.objects.get(id=test_case_id)
    assert test_case_obj.input_text == input_text
    assert test_case_obj.output_text == output_text
    assert test_case_obj.score == score
    assert test_case_obj.is_hidden == is_hidden
    assert storage_response == created_test_case_dto
