"""Representa a associação entre clubes e livros."""
from app.database.session import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class ClubBook(Base):
    """Modelo de associação entre clubes e livros."""

    __tablename__ = 'club_books'

    club_id: Mapped[int] = mapped_column(ForeignKey('clubs.id'), primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'), primary_key=True)
