from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.response import Response


def t(value: str) -> str:
    return gettext_lazy(value)


def validationError(exc):
    return serializers.ValidationError({"detail": t(str(exc))})


def serialize_request(request: Request):
    body = "<binary data>" if request.content_type.startswith("multipart/") else request.body.decode("utf-8")[:1000]

    return {
        "method": request.method,
        "path": request.get_full_path(),
        "remote_addr": request.META.get("REMOTE_ADDR", ""),
        "headers": {k: v for k, v in request.headers.items()},
        "body": body,
        "user_id": request.user.id if request.user.is_authenticated else None,
    }


def serialize_response(response: Response):
    return {
        "status_code": response.status_code,
        "headers": {k: v for k, v in response.headers.items()},
        "body": response.content.decode("utf-8")[:1000],
    }


def get_content_type_for_model(model, for_concrete_model=True) -> ContentType:
    return ContentType.objects.get_for_model(model, for_concrete_model)


def jwt_encode(user, is_refresh=False):
    raise NotImplementedError


def jwt_decode(token) -> dict | None:
    raise NotImplementedError


def jwt_is_valid(token) -> bool:
    raise NotImplementedError
