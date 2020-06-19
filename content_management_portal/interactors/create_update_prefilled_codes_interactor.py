from typing import List
from content_management_portal.interactors.presenters.presenter_interface\
    import PresenterInterface
from content_management_portal.interactors.storages\
    .prefilled_code_storage_interface import PrefilledCodeStorageInterface
from content_management_portal.interactors.storages\
    .question_storage_interface import QuestionStorageInterface
from content_management_portal.interactors.storages.dtos\
    import PrefilledCodeDto
from content_management_portal.interactors.mixins.question_validation \
    import QuestionValidationMixin


class CreateUpdatePrefilledCodesInteractor(QuestionValidationMixin):

    def __init__(self, presenter: PresenterInterface,
                 prefilled_code_storage: PrefilledCodeStorageInterface,
                 question_storage: QuestionStorageInterface):
        self.presenter = presenter
        self.question_storage = question_storage
        self.prefilled_code_storage = prefilled_code_storage

    def create_update_prefilled_codes(
            self, question_id: int,
            prefilled_codes_dto: List[PrefilledCodeDto]):
        self.validate_question_id(question_id=question_id)
        new_prefilled_codes_dto, update_prefilled_codes_dto =\
            self._get_new_and_update_prefilled_codes_dto(prefilled_codes_dto)
        if self._is_update_prefilled_codes_exist(update_prefilled_codes_dto):
            self._validations_for_update_prefilled_codes_dto(
                question_id, update_prefilled_codes_dto)
            self.prefilled_code_storage.update_prefilled_codes(
                question_id=question_id,
                prefilled_codes_dto=update_prefilled_codes_dto)
        self.prefilled_code_storage.create_prefilled_codes(
            prefilled_codes_dto=new_prefilled_codes_dto
        )
        prefilled_codes_dto = self.prefilled_code_storage\
            .get_prefilled_codes_to_question(question_id=question_id)
        return self.presenter.get_response_for_create_update_prefilled_codes(
            prefilled_codes_dto=prefilled_codes_dto
        )

    @staticmethod
    def _is_update_prefilled_codes_exist(
            prefilled_codes_dto: List[PrefilledCodeDto]):

        is_prefilled_codes_exists = len(prefilled_codes_dto)
        bool_field = False

        if is_prefilled_codes_exists:
            bool_field = True

        return bool_field

    def _validations_for_update_prefilled_codes_dto(
            self, question_id: int,
            prefilled_codes_dto: List[PrefilledCodeDto]):
        prefilled_code_ids = self._get_prefilled_code_ids(
            prefilled_codes_dto=prefilled_codes_dto
        )
        db_prefilled_code_ids = self.prefilled_code_storage\
            .get_database_prefilled_code_ids(prefilled_code_ids)
        sorted_update_prefilled_code_ids = sorted(prefilled_code_ids)
        is_invalid_prefilled_code = (
            not db_prefilled_code_ids == sorted_update_prefilled_code_ids
        )
        if is_invalid_prefilled_code:
            self.presenter.raise_exception_for_invalid_prefilled_code()

        self._validations_for_update_prefilled_codes_questions(
            question_id=question_id,
            prefilled_code_ids=prefilled_code_ids
        )

    def _validations_for_update_prefilled_codes_questions(
            self, question_id: int,prefilled_code_ids: List[int]):

        prefilled_code_question_ids = self.prefilled_code_storage\
            .get_prefilled_codes_question_ids(prefilled_code_ids)
        is_different_question =\
            not prefilled_code_question_ids == [question_id]
        if is_different_question:
            self.presenter.raise_exception_for_different_question()

    @staticmethod
    def _get_prefilled_code_ids(prefilled_codes_dto: List[PrefilledCodeDto]):

        return [
            prefilled_code_dto.id
            for prefilled_code_dto in prefilled_codes_dto
        ]

    def _get_new_and_update_prefilled_codes_dto(
            self, prefilled_codes_dto: List[PrefilledCodeDto]):

        new_prefilled_codes_dto, update_prefilled_codes_dto = [], []
        for prefilled_code_dto in prefilled_codes_dto:
            if self._check_for_update_prefilled_code_dto(prefilled_code_dto):
                update_prefilled_codes_dto.append(prefilled_code_dto)
            else:
                new_prefilled_codes_dto.append(prefilled_code_dto)
        return new_prefilled_codes_dto, update_prefilled_codes_dto

    @staticmethod
    def _check_for_update_prefilled_code_dto(
            prefilled_code_dto: PrefilledCodeDto):

        prefilled_code_id = prefilled_code_dto.id
        is_update_prefilled_code = prefilled_code_id
        response = False

        if is_update_prefilled_code:
            response = True

        return response
