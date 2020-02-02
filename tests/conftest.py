from typing import List, Optional

import pytest

from perfin.models.users import User
from perfin.repositories.abc import UsersRepository


@pytest.fixture
def user_data() -> dict:
    return {
        'username': 'admin',
        'password': 'password',
    }


@pytest.fixture
def user(user_data: dict) -> User:
    user = User(user_data['username'])
    user.set_password(user_data['password'])
    return user


@pytest.fixture
def stored_users(user: User) -> List[User]:
    return [user]


@pytest.fixture
def users_repository_mock(stored_users: List[User]):
    class UsersRepositoryMock(UsersRepository):
        async def get_all(self) -> List[User]:
            return stored_users

        async def get_by_username(self, username: str) -> Optional[User]:
            for user in stored_users:
                if user.username == username:
                    return user

        async def create(self, username: str, password: str) -> User:
            user = User(username=username)
            user.set_password(password)
            return user

    return UsersRepositoryMock()
