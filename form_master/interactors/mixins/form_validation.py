from form_master.interactors.storages.storage_interface \
    import StorageInterface
from form_master.exceptions.exceptions import FormClosed


class FormValidationMixin:

    def __init__(self, storage: StorageInterface):
        self.stoarge = storage

    def validate_for_live_form(self, form_id: int):
        form_status_dto = self.storage.get_form_status_dto(form_id=form_id)
        if not form_status_dto.is_live:
            raise FormClosed()
