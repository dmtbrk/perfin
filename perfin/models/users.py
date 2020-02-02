from dataclasses import dataclass

from perfin.security import generate_hash, verify_password


@dataclass
class User:
    username: str
    _password_hash: bytes = None

    @property
    def password_hash(self) -> bytes:
        return self._password_hash

    def __eq__(self, other):
        if type(other) == type(self):
            return other.username == self.username
        return NotImplemented

    def set_password(self, password: str) -> None:
        self._password_hash = generate_hash(password)

    def verify_password(self, password: str) -> bool:
        return verify_password(password, self.password_hash)
