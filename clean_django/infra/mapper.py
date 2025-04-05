from abc import ABC, abstractmethod

from clean_django.domain.dto import BaseDTO
from clean_django.domain.entity import Entity


class BaseMapper(ABC):
    @abstractmethod
    def to_dto(self, entity: Entity) -> BaseDTO: ...

    @abstractmethod
    def to_entity(self, dto: BaseDTO) -> Entity: ...
