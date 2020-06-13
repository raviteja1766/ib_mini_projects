from content_management_portal.presenters.presenter_implementation\
    import PresenterImplementation

def test_get_response_for_create_update_solution_approachs(
        solution_approach_dto, solution_approach_dto_response):

    # Arrange
    presenter = PresenterImplementation()

    # Act
    actual_response = presenter\
        .get_response_for_create_update_solution_approach(
            solution_approach_dto=solution_approach_dto
        )

    # Assert
    assert actual_response == solution_approach_dto_response
