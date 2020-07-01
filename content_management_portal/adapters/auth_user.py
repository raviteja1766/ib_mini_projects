from typing import List
from content_management_portal.dtos.dtos import UserDto


class AuthService:

    @property
    def interface(self):
        from user_app.interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_dtos(self, user_ids: List[int]):
        user_dtos = self.interface.get_user_dtos(user_ids=user_ids)

        user_dtos = [
            UserDto(user_id=user_dto.user_id, username=user_dto.username)
            for user_dto in user_dtos
        ]
        return user_dtos
