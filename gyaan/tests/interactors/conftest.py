import pytest
import datetime
from gyaan.interactors.storages.dtos import *
from gyaan.interactors.presenters.dtos import *


@pytest.fixture()
def post_dtos():

    return [
        PostDTO(
            post_id=1,
            posted_at=datetime.datetime(2012, 5, 6),
            posted_by_id=1,
            title="post_title",
            content="post_content"
        )
    ]

@pytest.fixture()
def post_tag_ids():
    return [
        PostTag(
            post_id=1,
            tag_id=1
        )
    ]

@pytest.fixture()
def tags():
    return [
        Tag(
            tag_id=1,
            name="tag_name"
        )
    ]

@pytest.fixture()
def posts_tags_dto(post_tag_ids, tags):

    return PostTagDetails(
        post_tag_ids=post_tag_ids,
        tags=tags
    )

@pytest.fixture()
def post_reaction_counts():

    return [PostReactionsCount(
        post_id=1,
        reactions_count=4
    )]

@pytest.fixture()
def comment_reaction_counts():

    return [
        CommentReactionsCount(
            comment_id=1,
            reactions_count=4
        ),
        CommentReactionsCount(
            comment_id=2,
            reactions_count=4
        )
    ]

@pytest.fixture()
def comment_counts():

    return [
        PostCommentsCount(
            post_id=1,
            comments_count=4
        )
    ]

@pytest.fixture()
def reply_counts():

    return [
        CommentRepliesCount(
            comment_id=1,
            replies_count=4
        ),
        CommentRepliesCount(
            comment_id=2,
            replies_count=4
        )
    ]

@pytest.fixture()
def comment_dtos():

    return [
        CommentDTO(
            comment_id=1,
            commented_at=datetime.datetime(2012, 5, 3),
            commented_by_id=1,
            content="comment_content"
        ),
        CommentDTO(
            comment_id=2,
            commented_at=datetime.datetime(2012, 5, 3),
            commented_by_id=1,
            content="comment_content"
        )
    ]

@pytest.fixture()
def users_dtos():

    return [
        UserDetailsDTO(
            user_id=1,
            name="user_1",
            profile_pic_url="profilepic_1"
        )
    ]

@pytest.fixture()
def complete_post_details(
        post_dtos, post_reaction_counts, comment_reaction_counts,
        comment_dtos, comment_counts, reply_counts, post_tag_ids,
        tags, users_dtos
        ):

    return CompletePostDetails(
        post_dtos=post_dtos,
        post_reaction_counts=post_reaction_counts,
        comment_reaction_counts=comment_reaction_counts,
        comment_counts=comment_counts,
        reply_counts=reply_counts,
        comment_dtos=comment_dtos,
        post_tag_ids=post_tag_ids,
        tags=tags,
        users_dtos=users_dtos
    )

# -------------------DomainDetails----------------------------------

@pytest.fixture()
def domain_dto():
    return DomainDTO(
        domain_id=1,
        name="domain_name",
        description="domain description"
    )

@pytest.fixture()
def domain_stats():
    return DomainStatsDTO(
        domain_id=1,
        followers_count=233,
        posts_count=1,
        bookmarked_count=234
    )

@pytest.fixture()
def domain_experts():
    return [
        UserDetailsDTO(
            user_id=2,
            name="user_1",
            profile_pic_url="profilepic_1"
        )
    ]

@pytest.fixture()
def join_requests():
    return [
        DomainJoinRequestDTO(
            request_id=2,
            user_id=3
        )
    ]

@pytest.fixture()
def requested_users():
    return [
        UserDetailsDTO(
            user_id=3,
            name="user_1",
            profile_pic_url="profilepic_1"
        )
    ]

@pytest.fixture()
def domain_details_dto(
        domain_dto, domain_stats, users_dtos,
        join_requests, requested_users):
    return DomainDetailsDTO(
        domain=domain_dto,
        domain_stats=domain_stats,
        domain_experts=users_dtos,
        join_requests=join_requests,
        requested_users=requested_users,
        user_id=1,
        is_user_domain_expert=True
    )


@pytest.fixture()
def user_not_domain_expert_details_dto(
        domain_dto, domain_stats, domain_experts):
    return DomainDetailsDTO(
        domain=domain_dto,
        domain_stats=domain_stats,
        domain_experts=domain_experts,
        join_requests=[],
        requested_users=[],
        user_id=1,
        is_user_domain_expert=False
    )


@pytest.fixture()
def domain_with_posts_dto(domain_details_dto, complete_post_details):

    return DomainDetailsWithPosts(
        post_details=complete_post_details,
        domain_details=domain_details_dto
    )
