from gyaan.exceptions.exceptions import UserNotDomainMember
from gyaan.interactors.storages.storage_interface \
    import StorageInterface


class UserDomainMemberValidationMixin:

    def validate_user_domain_member(self, user_id: int, domain_id: int):

        is_not_user_domain_follower = not self.storage\
            .is_user_following_domain(user_id=user_id, domain_id=domain_id)
        if is_not_user_domain_follower:
            raise UserNotDomainMember(user_id=user_id, domain_id=domain_id)