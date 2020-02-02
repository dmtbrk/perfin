import os
import hashlib


SALT_LENGTH = 32


def _generate_hash(password: bytes, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac(
        'sha256',
        password,
        salt,
        10 ** 5,
    )


def generate_hash(password: str) -> bytes:
    """Takes plain password and generates a hash-salt pair."""
    salt = os.urandom(SALT_LENGTH)
    password_hash = _generate_hash(password.encode('utf-8'), salt)
    return password_hash + salt


def verify_password(plain_password: str, password_hash: bytes) -> bool:
    """Checks if that plain_password was used for generating password_hash."""
    salt = password_hash[-SALT_LENGTH:]
    hash_original = password_hash[:-SALT_LENGTH]
    hash_generated = _generate_hash(plain_password.encode('utf-8'), salt)
    return hash_original == hash_generated
