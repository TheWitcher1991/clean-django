from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class AbstractRepository(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]: ...

    @abstractmethod
    def add(self, entity: T) -> T: ...

    @abstractmethod
    def save(self, entity: T) -> None: ...

    @abstractmethod
    def delete(self, entity: T) -> None: ...

    @abstractmethod
    def list(self) -> list[T]: ...
