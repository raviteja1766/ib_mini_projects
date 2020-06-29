class ServiceAdapter:

    @property
    def auth_service(self):
        from .auth_service import AuthService
        return AuthService()


def get_service_adapter():
    return ServiceAdapter()
