from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation
from content_management_portal.constants.enums import CodeLanguageType


def test_get_response_for_create_update_rough_solutions(
        rough_solutions_dtos):

    # Arrange
    presenter = PresenterImplementation()
    expected_response = {
        "question_id": 1,
        "rough_solutions": [
            {
                "rough_solution_id": 1,
                "file_name": "prime.py",
                "language": CodeLanguageType.PYTHON.value,
                "solution_content": "code_language"
            }
        ]
    }
    # Act
    actual_response = \
        presenter.get_response_for_base_create_update_solutions_wrapper(
            solutions_dto=rough_solutions_dtos
        )

    # Assert
    assert actual_response == expected_response
