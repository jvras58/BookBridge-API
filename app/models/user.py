"""Representa o modelo de usuário."""

from app.database.session import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash


class User(Base):
    """Modelo de usuarios."""

    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)

    def set_password(self, password: str) -> None:
        """Define a senha do usuário."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verifica se a senha está correta."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self) -> dict:
        """Converte o objeto User em um dicionário."""
        return {
            "id": self.id,
            "username": self.username,
        }
