import pytest
from freezegun import freeze_time
from content_management_portal.storages.hint_storage_implementation\
    import HintStorageImplementation
from content_management_portal.models import Hint
from content_management_portal.constants.enums import DescriptionType

@pytest.mark.django_db
def test_create_hint_given_hint_dto_creates_and_returns_dto(
        create_questions, new_hint_dto, created_hint_dto):

    # Arrange
    hint_id = 1
    title = "title_1"
    content = "content"
    content_type = DescriptionType.HTML.value
    hint_storage = HintStorageImplementation()

    # Act
    storage_response = hint_storage.create_hint(
        hint_dto=new_hint_dto
    )

    # Assert
    hint_obj = Hint.objects.get(id=hint_id)
    assert hint_obj.title == title
    assert hint_obj.content == content
    assert hint_obj.content_type == content_type
    assert storage_response == created_hint_dto
