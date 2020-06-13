from typing import List
from content_management_portal.interactors.storages.dtos\
    import PrefilledCodeDto
from content_management_portal.interactors.storages\
    .prefilled_code_storage_interface import PrefilledCodeStorageInterface
from content_management_portal.interactors\
    .create_update_prefilled_codes_interactor\
    import CreateUpdatePrefilledCodesInteractor
from content_management_portal.models import PrefilledCode, Question

class PrefilledCodeStorageImplementation(PrefilledCodeStorageInterface):

    def update_prefilled_codes(
            self,question_id: int,
            prefilled_codes_dto: List[PrefilledCodeDto]):

        prefilled_codes_dto_dict = {}

        for prefilled_code_dto in prefilled_codes_dto:
            prefilled_codes_dto_dict[prefilled_code_dto.id] =\
                prefilled_code_dto

        prefilled_code_objs = PrefilledCode.objects\
            .filter(question_id=question_id)

        for prefilled_code_obj in prefilled_code_objs:
            prefilled_code_dto =\
                prefilled_codes_dto_dict[prefilled_code_obj.id]
            self._update_single_prefilled_code(
                prefilled_code_obj, prefilled_code_dto)

        PrefilledCode.objects.bulk_update(
            prefilled_code_objs, ["file_name", "language", "code"]
        )

    @staticmethod
    def _update_single_prefilled_code(prefilled_code_obj, prefilled_code_dto):

        prefilled_code_obj.file_name=prefilled_code_dto.file_name
        prefilled_code_obj.language=prefilled_code_dto.language_type
        prefilled_code_obj.code=prefilled_code_dto.text_code

    def create_prefilled_codes(
            self, prefilled_codes_dto: List[PrefilledCodeDto]):

        PrefilledCode.objects.bulk_create([
            PrefilledCode(
                file_name=prefilled_code_dto.file_name,
                language=prefilled_code_dto.language_type,
                code=prefilled_code_dto.text_code,
                question_id=prefilled_code_dto.question_id,
                user_id=prefilled_code_dto.user_id
            ) for prefilled_code_dto in prefilled_codes_dto
        ])


    def get_prefilled_codes_to_question(
            self, question_id: int) -> List[PrefilledCodeDto]:

        prefilled_code_objs = PrefilledCode.objects\
            .filter(question_id=question_id)
        return [
            PrefilledCodeDto(
                id=prefilled_code_obj.id,
                file_name=prefilled_code_obj.file_name,
                language_type=prefilled_code_obj.language,
                text_code=prefilled_code_obj.code,
                question_id=prefilled_code_obj.question_id,
                user_id=prefilled_code_obj.user_id
            ) for prefilled_code_obj in prefilled_code_objs
        ]

    def get_database_prefilled_code_ids(
            self, prefilled_code_ids: List[int]) -> List[int]:

        prefilled_code_ids = PrefilledCode.objects\
            .filter(id__in=prefilled_code_ids)\
            .values_list('id', flat=True)

        return list(prefilled_code_ids)

    def get_prefilled_codes_question_ids(
            self, prefilled_code_ids: List[int]) -> List[int]:

        test_cases_question_ids = Question.objects\
            .filter(prefilledcode__id__in=prefilled_code_ids)\
            .values_list('id', flat=True)

        return list(set(test_cases_question_ids))

    def validate_prefilled_code(self, prefilled_code_id: int) -> bool:

        return PrefilledCode.objects.filter(id=prefilled_code_id).exists()

    def delete_prefilled_code(self, prefilled_code_id: int):

        PrefilledCode.objects.filter(id=prefilled_code_id).delete()

    def get_question_to_prefilled_code(self, prefilled_code_id: int) -> int:

        prefilled_code_obj = PrefilledCode.objects.get(id=prefilled_code_id)
        question_id = prefilled_code_obj.question_id
        return question_id
