from typing import List


class AuthService:
    @property
    def interface(self):
        from user_app.interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_dtos(self, user_ids: List[int]):
        user_dtos = self.interface.get_user_dtos(user_ids=user_ids)

        # TODO: Convert to DTO in this app
        return user_dtos
