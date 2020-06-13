import logging

from rest_framework.authentication import (BaseAuthentication)

logger = logging.getLogger(__name__)


class APIKeyAuthentication(BaseAuthentication):
    """Token based authentication using the JSON Web Token standard."""

    def __init__(self):
        super(APIKeyAuthentication, self).__init__()

    def authenticate(self, request):
        # user = parse_headers(request.META)
        # return user, None
        raise NotImplemented()
