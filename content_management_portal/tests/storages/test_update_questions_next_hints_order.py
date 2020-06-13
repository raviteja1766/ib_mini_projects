import pytest
from freezegun import freeze_time
from content_management_portal.storages.hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.constants.enums import DescriptionType
from content_management_portal.models import Hint


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_update_questions_next_hints_order_given_valid_updates_order(
        create_questions):

    # Assert
    Hint.objects.bulk_create([
        Hint(
            id=None, title="title_1", content_type=DescriptionType.HTML.value,
            content="content", order_id=1, question_id=1, user_id=1
        ),
        Hint(
            id=None, title="title_1", content_type=DescriptionType.HTML.value,
            content="content", order_id=2, question_id=1, user_id=1
        )
    ])
    question_id = 1
    order_id = 1
    hint_storage = HintStorageImplementation()

    # Act
    hint_storage.update_questions_next_hints_order(
        question_id=question_id, order_id=order_id
    )

    # Assert
    hint_obj = Hint.objects.get(id=2)
    assert hint_obj.order_id == order_id