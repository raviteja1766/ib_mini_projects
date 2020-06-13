import pytest
from freezegun import freeze_time
from content_management_portal.storages.prefilled_code_storage_implementation\
    import PrefilledCodeStorageImplementation
from content_management_portal.models import TestCase


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_prefilled_code_given_valid_prefilled_code_and_returns_true(
        create_prefilled_codes):

    # Arrange
    prefilled_code_id = 1
    prefilled_code_storage = PrefilledCodeStorageImplementation()
    expected_response = True

    # Act
    actual_response = prefilled_code_storage.validate_prefilled_code(
        prefilled_code_id=prefilled_code_id
    )

    # Assert
    assert actual_response == expected_response

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_prefilled_code_given_invalid_prefilled_code_and_returns_false(
        create_prefilled_codes):

    # Arrange
    prefilled_code_id = 2
    prefilled_code_storage = PrefilledCodeStorageImplementation()
    expected_response = False

    # Act
    actual_response = prefilled_code_storage.validate_prefilled_code(
        prefilled_code_id=prefilled_code_id
    )

    # Assert
    assert actual_response == expected_response
