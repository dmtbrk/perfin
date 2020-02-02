from perfin.repositories.abc import UsersRepository
from perfin.models.users import User


class UsersService:
    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository

    def register(self, username: str, password: str) -> User:
        pass
