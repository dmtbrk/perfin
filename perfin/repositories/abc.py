from abc import ABC, abstractmethod
from typing import List, Optional

from perfin.models.transactions import Transaction
from perfin.models.users import User


class BaseRepository(ABC):
    pass


class UsersRepository(BaseRepository):
    @abstractmethod
    async def get_all(self) -> List[User]:
        pass

    @abstractmethod
    async def get_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    async def create(self, username: str, password: str) -> User:
        pass


class TransactionsRepository(BaseRepository):
    @abstractmethod
    async def get_all(self) -> List[Transaction]:
        pass

    @abstractmethod
    async def get_by_user(self, user: User) -> List[Transaction]:
        pass

    @abstractmethod
    async def create(self, title: str, amount: int) -> Transaction:
        pass
