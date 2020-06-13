import datetime
from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.interactors.storages.dtos import TestCaseDto


def test_get_response_for_create_update_test_case_returns_access_token(
        test_case_dto, test_case_dto_response):
    
    # Arrange
    presenter = PresenterImplementation()
    
    # Act
    actual_response = presenter.get_response_for_create_update_test_case(
        test_case_dto=test_case_dto
    )
    
    # Assert
    assert actual_response == test_case_dto_response