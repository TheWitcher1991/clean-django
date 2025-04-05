from abc import ABC, abstractmethod


class AbstractDTO(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict): ...

    @abstractmethod
    def to_dict(self) -> dict: ...
