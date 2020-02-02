import pytest

from perfin.models.users import User
from perfin.repositories.abc import UsersRepository
from perfin.services.auth import AuthService


@pytest.fixture
def auth_service(users_repository_mock: UsersRepository) -> AuthService:
    return AuthService(users_repository_mock)


@pytest.mark.asyncio
async def test_register_new_user(auth_service: AuthService, user: User, user_data: dict):
    registered_user = await auth_service.register(username=user.username, password=user_data['password'])
    assert registered_user == user
    assert registered_user.verify_password(user_data['password'])
