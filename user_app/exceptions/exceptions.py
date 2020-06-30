from typing import List


class InvalidUsername(Exception):
    pass


class InvalidPassword(Exception):
    pass


class DuplicateUserIds(Exception):
    def __init__(self, user_ids: List[int]):
        self.user_ids = user_ids


class InvalidUserIds(Exception):
    def __init__(self, user_ids: List[int]):
        self.user_ids = user_ids