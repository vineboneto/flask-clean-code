from abc import ABCMeta, abstractmethod
from typing import Any


class UpdateRepo(metaclass=ABCMeta):
    @abstractmethod
    async def update(self, params) -> Any:
        raise NotImplementedError
