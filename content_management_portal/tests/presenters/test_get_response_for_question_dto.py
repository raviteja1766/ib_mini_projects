from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation


def test_get_response_for_question_dto_returns_question_dict(question_dto):

    # Arrange
    presenter = PresenterImplementation()
    expected_response = {
        "question_id": 1,
        "short_text": "short_text1",
        "problem_description": {
            "content_type": "HTML",
            "content": "description1"
        }
    }

    # Act
    actual_response = presenter.get_response_for_question_dto(question_dto)

    # Assert
    assert actual_response == expected_response