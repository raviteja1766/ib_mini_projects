import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class DomainDTO:
    domain_id: int
    name: str
    description: str


@dataclass
class DomainStatsDTO:
    domain_id: int
    followers_count: int
    posts_count: int
    bookmarked_count: int


@dataclass
class UserDetailsDTO:
    user_id: int
    name: str
    profile_pic_url: str


@dataclass
class DomainJoinRequestDTO:
    request_id: int
    user_id: int


@dataclass
class PostDTO:
    post_id: int
    posted_at: datetime.datetime
    posted_by_id: int
    title: str
    content: str


@dataclass
class CommentDTO:
    comment_id: int
    commented_at: datetime.datetime
    commented_by_id: int
    content: str


@dataclass
class Tag:
    tag_id: int
    name: str


@dataclass
class PostTag:
    post_id: int
    tag_id: int


@dataclass
class PostTagDetails:
    tags: List[Tag]
    post_tag_ids: List[PostTag]


@dataclass
class PostReactionsCount:
    post_id: int
    reactions_count: int


@dataclass
class CommentReactionsCount:
    comment_id: int
    reactions_count: int


@dataclass
class PostCommentsCount:
    post_id: int
    comments_count: int


@dataclass
class CommentRepliesCount:
    comment_id: int
    replies_count: int


@dataclass()
class CompletePostDetails:
    post_dtos: List[PostDTO]
    post_reaction_counts: List[PostReactionsCount]
    comment_reaction_counts: List[CommentReactionsCount]
    comment_counts: List[PostCommentsCount]
    reply_counts: List[CommentRepliesCount]
    comment_dtos: List[CommentDTO]
    post_tag_ids: List[PostTag]
    tags: List[Tag]
    users_dtos: List[UserDetailsDTO]
