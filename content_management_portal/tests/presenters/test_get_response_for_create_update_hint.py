import datetime
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation

def test_get_response_for_create_update_test_case_returns_access_token(
        hint_dto, hint_dto_response):

    # Arrange
    presenter = PresenterImplementation()

    # Act
    actual_response = presenter.get_response_for_create_update_hint(
        hint_dto=hint_dto
    )

    # Assert
    assert actual_response == hint_dto_response