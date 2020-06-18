from gyaan.exceptions.exceptions import (
    UserNotDomainMember, DomainDoesNotExist,
    InvalidOffsetValue, InvalidLimitValue
)
from gyaan.interactors.presenters.dtos import DomainDetailsWithPosts
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.get_domain_details_interactor \
    import GetDomainDetailsInteractor
from gyaan.interactors.get_domain_posts_interactor \
    import DomainPostsInteractor
from gyaan.constants.constants import *
from gyaan.interactors.mixins.user_domain_member_validation \
    import UserDomainMemberValidation


class GetDomainWithPostsInteractor(UserDomainMemberValidation):

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_with_posts_wrapper(self, user_id: int, domain_id: int,
                                      offset: int, limit: int,
                                      presenter: PresenterInterface):
        from gyaan.exceptions.exceptions import DomainDoesNotExist
        try:
            return self._get_domain_with_posts_response(
                user_id=user_id, domain_id=domain_id,
                offset=offset, limit=limit,
                presenter=presenter
            )
        except DomainDoesNotExist as err_obj:
            presenter.raise_exception_for_invalid_domain(error_obj=err_obj)
        except UserNotDomainMember as err_obj:
            presenter.raise_exception_for_user_not_domain_member(
                error_obj=err_obj
            )
        except InvalidOffsetValue:
            presenter.raise_exception_for_invalid_offset_value()
        except InvalidLimitValue:
            presenter.raise_exception_for_invalid_limit_value()

    def _get_domain_with_posts_response(self, user_id: int, domain_id: int,
                                        offset: int, limit: int,
                                        presenter: PresenterInterface):

        domain_with_posts_dto = self.get_domain_with_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        return presenter.get_domain_with_posts_response(
            domain_with_posts_dto=domain_with_posts_dto
        )

    def get_domain_with_posts(self, user_id: int, domain_id: int,
                              offset: int, limit: int):

        self.storage.validate_domain_id(domain_id=domain_id)
        self.validate_user_domain_member(user_id=user_id, domain_id=domain_id)
        offset, limit = self._validations_for_offset_and_limit(
            offset=offset, limit=limit
        )
        domain_details = self._get_domain_details(
            user_id=user_id, domain_id=domain_id
        )
        domain_posts = self._get_domain_posts(
            user_id=user_id, domain_id=domain_id,
            offset=offset, limit=limit
        )
        return DomainDetailsWithPosts(
            domain_details=domain_details,
            post_details=domain_posts
        )

    def _get_domain_posts(
            self, user_id: int, domain_id: int,
            offset: int, limit: int
            ):

        domain_posts_interactor = DomainPostsInteractor(
            storage=self.storage
        )
        domain_posts = domain_posts_interactor.get_domain_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )
        return domain_posts

    def _get_domain_details(self, user_id: int, domain_id: int):

        domain_details_interactor = GetDomainDetailsInteractor(
            storage=self.storage
        )

        domain_details = domain_details_interactor.get_domain_details(
            user_id=user_id,
            domain_id=domain_id
        )

        return domain_details

    @staticmethod
    def _validations_for_offset_and_limit(offset: int, limit: int):

        offset, limit = check_for_none_values_of_offset_and_limit(
            offset=offset, limit=limit
        )
        validate_offset(offset=offset)
        validate_limit(limit=limit)
        return offset, limit