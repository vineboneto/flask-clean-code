from abc import ABCMeta, abstractmethod
from typing import Any


class AddRepo(metaclass=ABCMeta):
    @abstractmethod
    async def add(self, params) -> Any:
        raise NotImplementedError
