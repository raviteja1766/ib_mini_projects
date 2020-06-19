from gyaan.exceptions.exceptions \
    import UserNotDomainMember, DomainDoesNotExist
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.exceptions.exceptions \
    import DomainDoesNotExist, UserNotDomainMember
from gyaan.constants.constants import *
from gyaan.interactors.get_posts_interactor import GetPostsInteractor
from gyaan.interactors.mixins.user_domain_member_validation \
    import UserDomainMemberValidationMixin

class DomainPostsInteractor(UserDomainMemberValidationMixin):

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_posts_wrapper(self, user_id: int, domain_id: int,
                                 offset: int, limit: int,
                                 presenter: PresenterInterface):

        try:
            return self._get_domain_posts_response(
                user_id=user_id, domain_id=domain_id, offset=offset,
                limit=limit, presenter=presenter
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


    def _get_domain_posts_response(self, user_id: int, domain_id: int,
                          offset: int, limit: int,
                          presenter: PresenterInterface):

        domain_posts_details = self.get_domain_posts(
            user_id=user_id, domain_id=domain_id,
            offset=offset, limit=limit
        )
        return presenter.get_response_for_get_domain_posts(
            posts_details=domain_posts_details
        )


    def get_domain_posts(self, user_id: int, domain_id: int,
                         offset: int, limit: int):

        self.storage.validate_domain_id(domain_id=domain_id)
        self.validate_user_domain_member(user_id=user_id, domain_id=domain_id)

        offset, limit = self._validations_for_offset_and_limit(
            offset=offset, limit=limit
        )
        post_ids = self.storage.get_domain_post_ids(
            domain_id=domain_id, offset=offset, limit=limit
        )

        get_posts_interactor = GetPostsInteractor(storage=self.storage)
        return get_posts_interactor.get_posts(post_ids=post_ids)

    @staticmethod
    def _validations_for_offset_and_limit(offset: int, limit: int):

        offset, limit = check_for_none_values_of_offset_and_limit(
            offset=offset, limit=limit
        )
        validate_offset(offset=offset)
        validate_limit(limit=limit)
        return offset, limit