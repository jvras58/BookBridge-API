"""Representa o modelo de livro."""
from datetime import datetime

from app.database.session import Base
from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class Book(Base):
    """Modelo de livros."""

    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String, nullable=False)
    author : Mapped[str] = mapped_column(String, nullable=False)
    created_by: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(),
        nullable=False, onupdate=func.now(),
    )

    def to_dict(self) -> dict:
        """Converte o objeto para um dicionário."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "created_by": self.created_by,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
