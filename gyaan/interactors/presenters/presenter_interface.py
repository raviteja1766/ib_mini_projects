from abc import ABC
from abc import abstractmethod
from typing import Optional, List, Dict
from gyaan.exceptions.exceptions import (
    InvalidPostIds, DuplicatePostIds, DomainDoesNotExist,
    UserNotDomainMember, InvalidLimitValue, InvalidOffsetValue
)
from gyaan.interactors.storages.dtos import CompletePostDetails
from gyaan.interactors.presenters.dtos import *


class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_post_ids(self, error_obj: InvalidPostIds):
        pass

    @abstractmethod
    def raise_exception_for_duplicate_post_ids(
            self, error_obj: DuplicatePostIds):
        pass

    @abstractmethod
    def raise_exception_for_invalid_domain(
            self, error_obj: DomainDoesNotExist):
        pass

    @abstractmethod
    def raise_exception_for_user_not_domain_member(
            self, error_obj: DomainDoesNotExist):
        pass

    @abstractmethod
    def raise_exception_for_invalid_offset_value(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_limit_value(self):
        pass

    @abstractmethod
    def get_response_for_get_domain_posts(
            self, posts_details: CompletePostDetails):
        pass

    @abstractmethod
    def get_response_for_get_domain_details(
            self,domain_details_dto: DomainDetailsDTO):
        pass

    @abstractmethod
    def get_domain_with_posts_response(
            self, domain_with_posts_dto: DomainDetailsWithPosts):
        pass