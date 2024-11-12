"""Representa a associação entre usuários e livros lidos em clubes."""
from app.database.session import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class UserBook(Base):
    """Modelo de associação entre usuários e livros lidos em clubes."""

    __tablename__ = 'user_books'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'), primary_key=True)
    club_id: Mapped[int] = mapped_column(ForeignKey('clubs.id'), primary_key=True)
