from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from clean_django.contracts.dto import AbstractDTO
from clean_django.domain.entity import Entity

T = TypeVar("T")


class AbstractMapper(ABC, Generic[T]):
    @abstractmethod
    def to_dto(self, entity: Entity) -> AbstractDTO: ...

    @abstractmethod
    def to_entity(self, dto: AbstractDTO) -> Entity: ...

    @staticmethod
    def to_instance(self, entity: Entity) -> T: ...
