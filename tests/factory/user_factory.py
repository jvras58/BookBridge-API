"""Arquivo Factory para testes do módulo usuario."""

import factory
from app.models.user import User


class UserFactory(factory.Factory):
    """Factory for User model."""

    class Meta:
        """Factory configuration."""

        model = User

    id = factory.Sequence(lambda n: n)
    username = factory.Faker('user_name')
    password_hash = factory.Faker('password')
