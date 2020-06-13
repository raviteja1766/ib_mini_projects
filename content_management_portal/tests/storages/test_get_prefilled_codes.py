import pytest
from content_management_portal.storages\
    .prefilled_code_storage_implementation\
    import PrefilledCodeStorageImplementation
from content_management_portal.models import PrefilledCode


@pytest.mark.django_db
def test_validate_get_prefilled_codes_given_valid_details_returns_details(
        create_prefilled_codes, prefilled_codes_dto):

    # Arrange
    question_id = 1
    prefilled_storage = PrefilledCodeStorageImplementation()

    # Act
    prefilled_storage_response = prefilled_storage\
        .get_prefilled_codes_to_question(question_id=question_id)

    # Assert
    assert prefilled_storage_response == prefilled_codes_dto
