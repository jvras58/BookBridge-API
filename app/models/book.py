"""Representa o modelo de livro."""

from app.database.session import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Book(Base):
    """Modelo de livros."""

    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)

    def to_dict(self) -> dict:
        """Converte o objeto Book em um dicionário."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
        }
