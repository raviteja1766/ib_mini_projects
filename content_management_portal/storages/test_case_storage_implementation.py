from typing import Optional, List
from django.db.models import Max
from content_management_portal.interactors.storages.dtos\
    import TestCaseDto, TestCaseSwapDto
from content_management_portal.interactors.storages\
    .test_case_storage_interface import TestCaseStorageInterface
from content_management_portal.models import TestCase, Question


class TestCaseStorageImplementation(TestCaseStorageInterface):

    def create_test_case(self, test_case_dto: TestCaseDto) -> TestCaseDto:

        test_case_obj = TestCase.objects.create(
            input_text=test_case_dto.input_text,
            output_text=test_case_dto.output_text,
            score=test_case_dto.score,
            is_hidden=test_case_dto.is_hidden,
            order_id=test_case_dto.order_id,
            question_id=test_case_dto.question_id,
            user_id=test_case_dto.user_id
        )
        test_case_dto.id = test_case_obj.id

        return test_case_dto

    def get_max_test_case_order_of_question(self, question_id: int):

        max_order = TestCase.objects\
            .filter(question_id=question_id)\
            .aggregate(order_id=Max('order_id'))

        return max_order['order_id']

    def update_test_case(self, test_case_dto: TestCaseDto) -> TestCaseDto:

        test_case_id = test_case_dto.id
        test_case_obj = TestCase.objects.get(id=test_case_id)
        test_case_obj.input_text=test_case_dto.input_text
        test_case_obj.output_text=test_case_dto.output_text
        test_case_obj.score=test_case_dto.score
        test_case_obj.is_hidden=test_case_dto.is_hidden
        test_case_obj.save()

        return test_case_dto

    def validate_test_case(self, test_case_id: int) -> bool:

        return TestCase.objects.filter(id=test_case_id).exists()

    def get_question_to_test_case(self, test_case_id: int) -> int:

        test_case_obj = TestCase.objects.get(id=test_case_id)

        return test_case_obj.question_id

    def delete_test_case_and_get_test_case_order(self, test_case_id: int):

        test_case_obj = TestCase.objects.get(id=test_case_id)
        order_id = test_case_obj.order_id
        test_case_obj.delete()
        return order_id


    def update_questions_next_test_cases_order(
            self, question_id: int, order_id: int):
        test_case_objs = TestCase.objects.filter(
            question_id=question_id,
            order_id__gte=order_id
        )

        for test_case_obj in test_case_objs:
            test_case_obj.order_id -= 1

        TestCase.objects.bulk_update(test_case_objs, ['order_id'])

    def update_test_cases_order(self, test_cases_dto: List[TestCaseSwapDto]):

        test_case_objs = TestCase.objects\
            .filter(id__in=[test_case.id for test_case in test_cases_dto])

        test_cases_dto_dict = {}

        for test_case_dto in test_cases_dto:
            test_cases_dto_dict[test_case_dto.id] = test_case_dto

        for test_case_obj in test_case_objs:
            test_case_dto = test_cases_dto_dict[test_case_obj.id]
            test_case_obj.order_id = test_case_dto.order_id

        TestCase.objects.bulk_update(test_case_objs, ['order_id'])

    def get_database_test_case_ids(
            self, test_case_ids: List[int]) -> List[int]:

        test_case_ids = TestCase.objects\
            .filter(id__in=test_case_ids)\
            .values_list('id',flat=True)
        return list(test_case_ids)

    def get_test_cases_question_ids(
            self, test_case_ids: List[int]) -> List[int]:

        question_ids = Question.objects\
            .filter(testcase__id__in=test_case_ids)\
            .values_list('id',flat=True)
        return list(set(question_ids))

