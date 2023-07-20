from typing import NamedTuple
from collections.abc import Iterator

from apps.homework.faker import faker


class User(NamedTuple):
    username: str
    email: str


def generate_user() -> User:
    return User(
        username=faker.first_name(),
        email=faker.email(),
    )


def generate_users(amount: int) -> Iterator[User]:
    for index in range(1, amount + 1):
        yield generate_user()