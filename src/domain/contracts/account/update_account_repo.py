from abc import ABCMeta, abstractmethod
from src.domain.models import Account


class UpdateAccountRepo(metaclass=ABCMeta):
    @abstractmethod
    async def update(self, params) -> Account:
        raise NotImplementedError
