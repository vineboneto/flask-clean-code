from abc import ABCMeta, abstractmethod
from typing import Any


class LoadByIdRepo(metaclass=ABCMeta):
    @abstractmethod
    async def load_by_id(self, id: int) -> Any:
        raise NotImplementedError
