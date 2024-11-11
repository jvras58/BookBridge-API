"""Representa o modelo de usuário."""
from datetime import datetime

from app.database.session import Base
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash


class User(Base):
    """Modelo de usuarios."""

    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(),
        nullable=False, onupdate=func.now(),
    )

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
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
