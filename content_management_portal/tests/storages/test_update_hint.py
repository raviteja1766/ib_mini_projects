import pytest
from freezegun import freeze_time
from content_management_portal.storages.hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.models import Hint
from content_management_portal.constants.enums import DescriptionType


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_hint_given_hint_dto_updates_and_returns_dto(
        update_hint_dto, create_hints):

    # Arrange
    hint_id = 1
    title="update_title_1"
    content_type=DescriptionType.HTML.value
    content="update_content"
    hint_storage = HintStorageImplementation()

    # Act
    storage_response = hint_storage.update_hint(
        hint_dto=update_hint_dto
    )

    # Assert
    hint_obj = Hint.objects.get(id=hint_id)
    assert hint_obj.title == title
    assert hint_obj.content_type == content_type
    assert hint_obj.content == content
    assert storage_response == update_hint_dto
