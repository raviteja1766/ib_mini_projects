from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.constants.enums import CodeLanguageType

def test_get_response_for_create_update_clean_solutions(
        clean_solutions_dto):

    # Arrange
    presenter = PresenterImplementation()
    expected_response = {
        "question_id": 1,
        "clean_solutions": [
            {
                "clean_solution_id": 1,
                "file_name": "prime.py",
                "language": CodeLanguageType.PYTHON.value,
                "solution_content": "code_language"
            }
        ]
    }

    # Act
    actual_response = presenter\
        .get_response_for_create_update_clean_solutions(
            clean_solutions_dto=clean_solutions_dto
        )

    # Assert
    assert actual_response == expected_response
