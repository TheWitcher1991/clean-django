import re

from clean_django.shared.core import ValueObject
from clean_django.shared.kernel.errors import Errors


class Email(ValueObject):
    value: str
    validation_regex = r"^[\w-\.]{1,40}@([\w-]+\.)+[\w-]{2,4}$"

    def __init__(self, value: str):
        self.value = value

    @staticmethod
    def create(value: str):
        if not re.match(Email.validation_regex, value):
            return Errors.value_is_invalid(value)

        return Email(value)
