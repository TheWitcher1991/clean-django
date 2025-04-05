from abc import ABC, abstractmethod


class BaseDTO(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict): ...

    @abstractmethod
    def to_dict(self) -> dict: ...
