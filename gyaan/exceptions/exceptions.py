from typing import List


class InvalidPostIds(Exception):
    def __init__(self, post_ids: List[int]):
        self.post_ids = post_ids


class DuplicatePostIds(Exception):
    def __init__(self, duplicate_ids: List[int]):
        self.duplicate_ids = duplicate_ids


class UserNotDomainMember(Exception):
    def __init__(self, user_id: int, domain_id: int):
        self.user_id = user_id
        self.domain_id = domain_id


class DomainDoesNotExist(Exception):
    def __init__(self, domain_id: int):
        self.domain_id = domain_id


class InvalidOffsetValue(Exception):
    pass


class InvalidLimitValue(Exception):
    pass



