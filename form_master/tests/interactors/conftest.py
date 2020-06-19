import pytest
from form_master.interactors.storages.dtos import *


@pytest.fixture()
def form_status_false():

    return FormStatusDto(
        form_id=1,
        is_live=False
    )

@pytest.fixture()
def form_status_true():

    return FormStatusDto(
        form_id=1,
        is_live=True
    )

@pytest.fixture()
def user_response_dto():

    return UserResponseDTO(
        user_id=1,
        question_id=1,
        option_id=1
    )

@pytest.fixture()
def user_text_response_dto():

    return UserTextResponseDTO(
        user_id=1,
        question_id=1,
        text="text"
    )
