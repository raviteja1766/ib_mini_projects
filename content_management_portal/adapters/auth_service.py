from typing import List
from content_management_portal.interactors.presenters.dtos \
    import UserDto
from content_management_portal.exceptions.exceptions \
    import InvalidCMPUserIds, DuplicateCMPUserIds
from user_app.exceptions.exceptions import InvalidUserIds, DuplicateUserIds


class AuthService:

    @property
    def interface(self):
        from user_app.interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_dtos(self, user_ids: List[int]):

        user_dtos = []
        try:
            user_dtos = self.interface.get_user_dtos(user_ids=user_ids)
        except InvalidUserIds:
            raise InvalidCMPUserIds
        except DuplicateUserIds:
            raise DuplicateCMPUserIds
        user_dtos = [
            UserDto(
                user_id=user_dto.user_id,
                username=user_dto.username,
            )
            for user_dto in user_dtos
        ]
        return user_dtos
