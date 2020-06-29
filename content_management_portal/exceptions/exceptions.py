from typing import List

class InvalidPostId(Exception):
    pass


class InvalidUserId(Exception):
    pass


class InvalidQuestionId(Exception):
    pass


class InvalidRoughSolution(Exception):
    pass


class RoughSolutionsQuestionMisMatch(Exception):
    pass


class DuplicateUserIds(Exception):
    def __init__(self, user_ids: List[int]):
        self.user_ids = user_ids


class InvalidUserIds(Exception):
    def __init__(self, user_ids: List[int]):
        self.user_ids = user_ids