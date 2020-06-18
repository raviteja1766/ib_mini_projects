from abc import ABC
from abc import abstractmethod
from typing import Optional, List, Dict
from gyaan.interactors.storages.dtos import *

class StorageInterface(ABC):

    @abstractmethod
    def get_valid_post_ids(self, post_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_posts_details(self, post_ids: List[int]) -> List[PostDTO]:
        pass

    @abstractmethod
    def get_posts_tags(self, post_ids: List[int]) -> PostTagDetails:
        pass

    @abstractmethod
    def get_posts_comments_count(
            self, post_ids: List[int]) -> List[PostCommentsCount]:
        pass

    @abstractmethod
    def get_posts_reactions_count(
            self, post_ids: List[int]) -> List[PostReactionsCount]:
        pass

    @abstractmethod
    def get_latest_comment_ids_to_posts(
            self, post_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_comments_details(
            self, comment_ids: List[int]) -> List[CommentDTO]:
        pass

    @abstractmethod
    def get_comment_reactions_count(
            self, comment_ids: List[int]) -> List[CommentReactionsCount]:
        pass

    @abstractmethod
    def get_comments_replies_count(
            self, comment_ids: List[int]) -> List[CommentRepliesCount]:
        pass

    @abstractmethod
    def get_users_details(self, user_ids: List[int]) -> List[UserDetailsDTO]:
        pass


    # Domain-storage
    @abstractmethod
    def validate_domain_id(self, domain_id: int):
        pass

    @abstractmethod
    def is_user_following_domain(self, user_id: int, domain_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_post_ids(self, domain_id: int, offset: int,
                            limit: int) -> List[int]:
        pass


    #Domain-Details
    @abstractmethod
    def get_domain_dto(self, domain_id: int) -> DomainDTO:
        pass

    @abstractmethod
    def get_domain_stats(self, domain_id: int) -> DomainStatsDTO:
        pass

    @abstractmethod
    def get_domain_expert_ids(self, domain_id: int) -> List[int]:
        pass

    @abstractmethod
    def is_user_domain_expert(self, user_id: int, domain_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_join_requests(
            self, domain_id: int) -> List[DomainJoinRequestDTO]:
        pass
