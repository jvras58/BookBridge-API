"""Módulo para gerenciar a sessão do banco de dados."""

from contextlib import contextmanager

from app.config.settings import get_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    scoped_session,
    sessionmaker,
)


class Base(DeclarativeBase):
    """Classe base para os modelos do banco de dados."""

engine = create_engine(get_settings().DB_URL)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

@contextmanager
def get_session() -> scoped_session:
    """Retorna uma sessão do banco de dados."""
    session = Session()
    try:
        yield session
    finally:
        session.close()
