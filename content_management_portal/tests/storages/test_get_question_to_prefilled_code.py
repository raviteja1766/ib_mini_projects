import pytest
from freezegun import freeze_time
from content_management_portal.storages.prefilled_code_storage_implementation\
    import PrefilledCodeStorageImplementation

@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_get_question_to_prefilled_code_given_prefilled_code_returns_question_id(
        create_prefilled_codes):

    # Assert
    prefilled_code_id = 1
    question_id = 1
    prefilled_code_storage = PrefilledCodeStorageImplementation()

    # Act
    response_id = prefilled_code_storage.get_question_to_prefilled_code(
        prefilled_code_id=prefilled_code_id
    )

    # Assert
    assert response_id == question_id