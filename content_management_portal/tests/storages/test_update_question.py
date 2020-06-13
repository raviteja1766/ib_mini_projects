from content_management_portal.storages.question_storage_implementation\
    import QuestionStorageImplementation
import pytest
from freezegun import freeze_time
from datetime import datetime
from content_management_portal.interactors.storages.dtos\
    import QuestionDto
from content_management_portal.constants.enums import DescriptionType


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_create_given_valid_details_returns_question_dto(
        create_questions):

    # Arrange
    question_dto = QuestionDto(
        id=1, short_text="short_text1",
        text_type=DescriptionType.HTML.value,
        description="description2",
        created_at=datetime(2012, 1,13),
        user_id=1
    )
    question_storage = QuestionStorageImplementation()

    # Act
    actual_dto = question_storage.update_question(
        question_dto=question_dto)

    # Assert
    assert actual_dto == question_dto
