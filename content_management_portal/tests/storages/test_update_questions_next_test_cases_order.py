import pytest
from freezegun import freeze_time
from content_management_portal.storages.test_case_storage_implementation\
    import TestCaseStorageImplementation
from content_management_portal.models import TestCase


@pytest.mark.django_db
@freeze_time("2012-01-13")
def test_delete_test_case_given_valid_deletes_test_case(create_questions):

    TestCase.objects.bulk_create([
        TestCase(
            input_text="first input", output_text="first output", score=75,
            is_hidden=False, question_id=1, user_id=1, order_id=1
        ),
        TestCase(
            input_text="first input", output_text="first output", score=75,
            is_hidden=False, question_id=1, user_id=1, order_id=2
        )
    ])
    # Assert
    question_id = 1
    order_id = 1
    test_case_storage = TestCaseStorageImplementation()

    # Act
    test_case_storage.update_questions_next_test_cases_order(
        question_id=question_id, order_id=order_id
    )

    # Assert
    test_case_obj = TestCase.objects.get(id=2)
    assert test_case_obj.order_id == order_id
