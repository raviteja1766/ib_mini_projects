import pytest
from freezegun import freeze_time
from content_management_portal.storages\
    .prefilled_code_storage_implementation\
    import PrefilledCodeStorageImplementation
from content_management_portal.models import PrefilledCode


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_delete_prefilled_code_given_valid_deletes_prefilled_code(
        create_prefilled_codes):

    # Assert
    prefilled_code_id = 1
    prefilled_code_storage = PrefilledCodeStorageImplementation()

    # Act
    prefilled_code_storage\
        .delete_prefilled_code(prefilled_code_id=prefilled_code_id)

    # Assert
    assert PrefilledCode.objects\
        .filter(id=prefilled_code_id).exists() == False
