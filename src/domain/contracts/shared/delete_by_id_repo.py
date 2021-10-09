from abc import ABCMeta, abstractmethod
from typing import Any


class DeleteByIdRepo(metaclass=ABCMeta):
    @abstractmethod
    async def delete(self, id: int) -> Any:
        raise NotImplementedError
