from typing import List

from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.exceptions.exceptions import InvalidPostIds, DuplicatePostIds
from gyaan.interactors.storages.dtos import CompletePostDetails


class GetPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def get_posts_wrapper(self, post_ids: List[int],
                          presenter: PresenterInterface):
        try:
            return self.get_posts(post_ids=post_ids)
        except InvalidPostIds as err_obj:
            presenter.raise_exception_for_invalid_post_ids(error_obj=err_obj)
        except DuplicatePostIds as err_obj:
            presenter.raise_exception_for_duplicate_post_ids(error_obj=err_obj)


    def get_posts(self, post_ids: List[int]):

        self._validation_for_duplicate_post_ids(post_ids=post_ids)
        self._validation_for_post_ids(post_ids=post_ids)

        posts_dto = self.storage.get_posts_details(post_ids=post_ids)
        posts_tags_dto = self.storage.get_posts_tags(post_ids=post_ids)
        posts_comments_count = \
            self.storage.get_posts_comments_count(post_ids=post_ids)
        posts_reactions_count = \
            self.storage.get_posts_reactions_count(post_ids=post_ids)

        comment_ids = self.storage\
            .get_latest_comment_ids_to_posts(post_ids=post_ids)
        comments_dto, comments_reactions_count, comments_replies_count,\
            user_ids = self._get_comments_details(comment_ids=comment_ids)

        user_ids += [ post_dto.posted_by_id for post_dto in posts_dto ]
        user_ids = self._get_unique_user_ids(user_ids=user_ids)
        user_dtos = self.storage.get_users_details(user_ids=user_ids)

        return CompletePostDetails(
            post_dtos=posts_dto,
            post_reaction_counts=posts_reactions_count,
            comment_reaction_counts=comments_reactions_count,
            comment_counts=posts_comments_count,
            reply_counts=comments_replies_count,
            comment_dtos=comments_dto,
            post_tag_ids=posts_tags_dto.post_tag_ids,
            tags=posts_tags_dto.tags,
            users_dtos=user_dtos
        )

    def _get_comments_details(self, comment_ids: List[int]):

        comments_dto = \
            self.storage.get_comments_details(comment_ids=comment_ids)
        comments_reactions_count = \
            self.storage.get_comment_reactions_count(comment_ids=comment_ids)
        comments_replies_count = \
            self.storage.get_comments_replies_count(comment_ids=comment_ids)
        user_ids = [ 
            comment_dto.commented_by_id for comment_dto in comments_dto
        ]

        return (
            comments_dto, comments_reactions_count,
            comments_replies_count, user_ids
        )


    def _validation_for_post_ids(self, post_ids: List[int]):

        db_post_ids = self.storage.get_valid_post_ids(post_ids=post_ids)
        invalid_post_ids = [
            post_id for post_id in post_ids if post_id not in db_post_ids
        ]
        is_invalid_post_ids_present = invalid_post_ids
        if is_invalid_post_ids_present:
            raise InvalidPostIds(post_ids=invalid_post_ids)

    @staticmethod
    def _validation_for_duplicate_post_ids(post_ids: List[int]):

        from collections import Counter

        duplicate_ids = [
            post_id for post_id, count in Counter(post_ids).items() if count>1
        ]

        is_duplicate_ids_present = duplicate_ids
        if is_duplicate_ids_present:
            raise DuplicatePostIds(duplicate_ids=duplicate_ids)

    @staticmethod
    def _get_unique_user_ids(user_ids: List[int]):

        return list(set(user_ids))