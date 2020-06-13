from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation


def test_get_response_for_complete_question_details_returns_details(
        question_complete_details_dto,
        question_complete_details_dto_response):

    # Arrange
    (
        question_dto, rough_solutions_dto, test_cases_dto,
        prefilled_codes_dto, solution_approach_dto,
        clean_solutions_dto, hints_dto
    ) = question_complete_details_dto
    presenter = PresenterImplementation()

    # Act
    actual_response = presenter.get_response_for_complete_question_details(
        question_dto=question_dto,
        rough_solutions_dto=rough_solutions_dto,
        test_cases_dto=test_cases_dto,
        prefilled_codes_dto=prefilled_codes_dto,
        solution_approach_dto=solution_approach_dto,
        clean_solutions_dto=clean_solutions_dto,
        hints_dto=hints_dto
    )

    # Assert
    assert actual_response == question_complete_details_dto_response
