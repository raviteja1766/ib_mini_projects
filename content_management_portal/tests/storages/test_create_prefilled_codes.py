import pytest
from content_management_portal.storages\
    .prefilled_code_storage_implementation\
    import PrefilledCodeStorageImplementation
from content_management_portal.models import PrefilledCode


@pytest.mark.django_db
def test_validate_create_prefilled_code_given_valid_details_returns_ids(
        create_prefilled_codes, new_prefilled_codes_dto):

    # Arrange
    prefilled_id = 1
    prefilled_storage = PrefilledCodeStorageImplementation()

    # Act
    prefilled_storage.create_prefilled_codes(
        prefilled_codes_dto=new_prefilled_codes_dto)

    # Assert
    assert PrefilledCode.objects.filter(id=prefilled_id).exists() == True
