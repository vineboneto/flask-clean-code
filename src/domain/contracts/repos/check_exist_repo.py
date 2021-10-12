from abc import ABCMeta, abstractmethod
from typing import Any


class CheckExistRepo(metaclass=ABCMeta):
    @abstractmethod
    async def check(self, value) -> bool:
        raise NotImplementedError
