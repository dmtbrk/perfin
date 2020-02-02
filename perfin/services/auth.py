from perfin.models.users import User
from perfin.repositories.abc import UsersRepository


class AuthenticationError(Exception):
    pass


class AuthService:
    def __init__(self, users_repository: UsersRepository):
        self.users_repository: UsersRepository = users_repository

    async def register(self, username: str, password: str) -> User:
        user = await self.users_repository.create(username, password)
        return user

    async def login(self, username: str, password: str) -> User:
        user = await self.users_repository.get_by_username(username)
        if user.verify_password(password):
            return user
        else:
            raise AuthenticationError('Incorrect password.')
