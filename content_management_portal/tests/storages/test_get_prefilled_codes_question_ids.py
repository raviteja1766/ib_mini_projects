import pytest
from content_management_portal.storages\
    .prefilled_code_storage_implementation\
    import PrefilledCodeStorageImplementation
from content_management_portal.models import PrefilledCode


@pytest.mark.django_db
def test_get_prefilled_codes_question_ids_given_valid_details_returns_ids(
        create_prefilled_codes):

    # Arrange
    prefilled_code_ids = [1]
    question_ids = [1]
    prefilled_storage = PrefilledCodeStorageImplementation()

    # Act
    db_question_ids = prefilled_storage\
        .get_prefilled_codes_question_ids(
            prefilled_code_ids=prefilled_code_ids
        )

    # Assert
    assert db_question_ids == question_ids
