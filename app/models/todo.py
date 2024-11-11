"""Modelo de item de todo."""

from app.database.session import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class TodoItem(Base):
    """Modelo de item de todo."""

    __tablename__ = 'todo_items'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task: Mapped[str] = mapped_column(String, nullable=False)
    completed: Mapped[int] = mapped_column(Integer, default=0)
