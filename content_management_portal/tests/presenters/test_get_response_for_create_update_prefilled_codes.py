from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.constants.enums import CodeLanguageType

def test_get_response_for_create_update_prefilled_codes(
        prefilled_codes_dto):

    # Arrange
    presenter = PresenterImplementation()
    expected_response = {
        "question_id": 1,
        "prefilled_codes": [
            {
                "language": CodeLanguageType.PYTHON.value,
                "solution_content": "code_language",
                "file_name": "prime.py",
                "prefilled_code_id": 1
            }
        ]
    }

    # Act
    actual_response = presenter\
        .get_response_for_create_update_prefilled_codes(
            prefilled_codes_dto=prefilled_codes_dto
        )

    # Assert
    assert actual_response == expected_response
