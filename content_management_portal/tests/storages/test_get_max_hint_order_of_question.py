import pytest
from freezegun import freeze_time
from content_management_portal.storages.hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.models import Hint
from content_management_portal.constants.enums import DescriptionType


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_max_hint_order_given_question_id_returns_order_id(
        create_hints):

    # Arrange
    order_id = 1
    question_id = 1
    hint_storage = HintStorageImplementation()

    # Act
    storage_response = hint_storage.get_max_hint_order_of_question(
        question_id=question_id
    )

    # Assert
    assert storage_response == order_id


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_max_hint_order_given_question_id_hint_not_exists_returns_none(
        create_questions):

    # Arrange
    order_id = None
    question_id = 1
    hint_storage = HintStorageImplementation()

    # Act
    storage_response = hint_storage.get_max_hint_order_of_question(
        question_id=question_id
    )

    # Assert
    assert storage_response == order_id