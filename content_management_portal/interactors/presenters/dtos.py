

from dataclasses import dataclass


@dataclass()
class UserDto:
    user_id: int
    name: str
    profile_pic: str
