from typing import List

import pytest
from pytest_mock import MockFixture

from perfin.repositories.abc import UsersRepository
from perfin.models.users import User
from perfin.services.users import UsersService


@pytest.mark.asyncio
async def test_register_new_user(users_repository_mock: UsersRepository, stored_users: List[User]):
    pass
