from typing import Optional, List
from django.db.models import Max
from content_management_portal.interactors.storages.dtos\
    import HintDto, HintSwapDto
from content_management_portal.interactors.storages\
    .hint_storage_interface import HintStorageInterface
from content_management_portal.models import Hint, Question


class HintStorageImplementation(HintStorageInterface):

    def create_hint(self, hint_dto: HintDto) -> HintDto:

        hint_obj = Hint.objects.create(
            title=hint_dto.title,
            content_type=hint_dto.content_type,
            content=hint_dto.content,
            order_id=hint_dto.order_id,
            question_id=hint_dto.question_id,
            user_id=hint_dto.user_id
        )
        hint_dto.id = hint_obj.id

        return hint_dto

    def get_max_hint_order_of_question(self, question_id: int):

        max_order = Hint.objects\
            .filter(question_id=question_id)\
            .aggregate(order_id=Max('order_id'))

        return max_order['order_id']

    def update_hint(self, hint_dto: HintDto) -> HintDto:

        hint_id = hint_dto.id
        hint_obj = Hint.objects.get(id=hint_id)
        hint_obj.title=hint_dto.title
        hint_obj.content_type=hint_dto.content_type
        hint_obj.content=hint_dto.content
        hint_obj.save()

        return hint_dto

    def validate_hint(self, hint_id: int) -> bool:

        return Hint.objects.filter(id=hint_id).exists()

    def get_question_to_hint(self, hint_id: int) -> int:

        hint_obj = Hint.objects.get(id=hint_id)

        return hint_obj.question_id

    def delete_hint_and_get_hint_order(self, hint_id: int):

        hint_obj = Hint.objects.get(id=hint_id)
        order_id = hint_obj.order_id
        hint_obj.delete()
        return order_id

    def update_questions_next_hints_order(self, question_id: int,
                                          order_id: int):
        hint_objs = Hint.objects.filter(
            question_id=question_id, order_id__gte=order_id
        )

        for hint_obj in hint_objs:
            hint_obj.order_id -= 1

        Hint.objects.bulk_update(hint_objs, ['order_id'])

    def update_hints_order(self, hints_dto: List[HintSwapDto]):

        hint_objs = Hint.objects\
            .filter(id__in=[hint.id for hint in hints_dto])

        hints_dto_dict = {}

        for hint_dto in hints_dto:
            hints_dto_dict[hint_dto.id] = hint_dto

        for hint_obj in hint_objs:
            hint_dto = hints_dto_dict[hint_obj.id]
            hint_obj.order_id = hint_dto.order_id

        Hint.objects.bulk_update(hint_objs, ['order_id'])

    def get_database_hint_ids(
            self, hint_ids: List[int]) -> List[int]:

        hint_ids = Hint.objects\
            .filter(id__in=hint_ids)\
            .values_list('id',flat=True)
        return list(hint_ids)

    def get_hints_question_ids(
            self, hint_ids: List[int]) -> List[int]:

        question_ids = Question.objects\
            .filter(hint__id__in=hint_ids)\
            .values_list('id',flat=True)
        return list(set(question_ids))
