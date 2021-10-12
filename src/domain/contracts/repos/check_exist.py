from abc import ABCMeta, abstractmethod
from typing import Any


class CheckExist(metaclass=ABCMeta):
    @abstractmethod
    async def check(self, value) -> bool:
        raise NotImplementedError
