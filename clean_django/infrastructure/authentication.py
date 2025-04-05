from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request

from clean_django.shared.kernel import t
from clean_django.shared.services import JWTService


class BaseAPIAuthentication(TokenAuthentication):
    keyword = "Bearer"
    model = None

    def authenticate(self, request: Request):
        return super().authenticate(request)

    def authenticate_credentials(self, key: str):
        return super().authenticate_credentials(key)

    def authenticate_header(self, request: Request):
        return super().authenticate_header(request)

    def get_auth_header(self, request: Request) -> str:
        auth_header = request.headers.get("Authorization", b"")
        return auth_header

    def get_token(self, auth_header) -> str | None:
        try:
            prefix, token = auth_header.split()
            return token
        except (ValueError, AttributeError):
            return None

    def get_prefix_and_token(self, auth_header) -> tuple[str, str] | tuple[None, None]:
        try:
            prefix, token = auth_header.split()
            return prefix, token
        except (ValueError, AttributeError):
            return None, None

    def get_user(self, user_id: int):
        raise NotImplementedError()


class APIAuthentication(BaseAPIAuthentication):
    def authenticate(self, request):
        auth_header = self.get_auth_header(request)

        if not auth_header:
            raise AuthenticationFailed(t("Authorization header not found"))

        prefix, token = self.get_prefix_and_token(auth_header)

        if not prefix or not token:
            raise AuthenticationFailed(t(f"Invalid authorization header. Expected '{self.keyword} <access_token>'"))

        if prefix.lower() != self.keyword.lower():
            raise AuthenticationFailed(t(f'Invalid authorization header. Expected "{self.keyword} <access_token>"'))

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        decoded_payload = JWTService.decode(key)

        if not decoded_payload:
            raise AuthenticationFailed(t("Access token not valid"))

        user_id = decoded_payload.get("user_id")
        if not user_id:
            raise AuthenticationFailed(t("Invalid token payload: missing user_id"))

        user = self.get_user(user_id)

        return user, decoded_payload
