from gyaan.exceptions.exceptions import UserNotDomainMember
from gyaan.interactors.presenters.dtos import DomainDetailsDTO
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.exceptions.exceptions import (
    DomainDoesNotExist, UserNotDomainMember
)
from gyaan.interactors.mixins.user_domain_member_validation \
    import UserDomainMemberValidationMixin


class GetDomainDetailsInteractor(UserDomainMemberValidationMixin):

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_details_wrapper(self, user_id: int, domain_id: int,
                                   presenter: PresenterInterface):

        try:
            return self._get_domain_details_wrapper(
                user_id=user_id, domain_id=domain_id, presenter=presenter
            )
        except DomainDoesNotExist as err_obj:
            presenter.raise_exception_for_invalid_domain(error_obj=err_obj)
        except UserNotDomainMember as err_obj:
            presenter.raise_exception_for_user_not_domain_member(
                error_obj=err_obj
            )

    def _get_domain_details_wrapper(self, user_id: int, domain_id: int,
                                   presenter: PresenterInterface):

        domain_details_dto = self.get_domain_details(
            user_id=user_id, domain_id=domain_id
        )
        return presenter.get_response_for_get_domain_details(
            domain_details_dto=domain_details_dto
        )


    def get_domain_details(self, user_id: int, domain_id: int):

        self.storage.validate_domain_id(domain_id=domain_id)
        self.validate_user_domain_member(user_id=user_id, domain_id=domain_id)

        domain_dto = self.storage.get_domain_dto(domain_id=domain_id)
        domain_stats = self.storage.get_domain_stats(domain_id=domain_id)
        domain_expert_ids = \
            self.storage.get_domain_expert_ids(domain_id=domain_id)
        domain_experts = \
            self.storage.get_users_details(user_ids = domain_expert_ids)
        is_user_domain_expert, domain_join_requests, requested_user_dtos = \
            self._get_domain_expert_details(
                user_id=user_id, domain_id=domain_id
            )
        return DomainDetailsDTO(
            domain=domain_dto,
            domain_stats=domain_stats,
            domain_experts=domain_experts,
            user_id=user_id,
            is_user_domain_expert=is_user_domain_expert,
            join_requests=domain_join_requests,
            requested_users=requested_user_dtos
        )


    def _get_domain_expert_details(self, user_id: int, domain_id: int):

        is_user_domain_expert = self.storage.is_user_domain_expert(
            user_id=user_id, domain_id=domain_id
        )
        domain_join_requests = []
        requested_user_dtos = []
        if is_user_domain_expert:
            domain_join_requests = self.storage.get_domain_join_requests(
                domain_id=domain_id
            )

        if domain_join_requests:
            user_ids = [ dto.user_id for dto in domain_join_requests ]
            requested_user_dtos = \
                self.storage.get_users_details(user_ids=user_ids)

        return is_user_domain_expert, domain_join_requests, requested_user_dtos
