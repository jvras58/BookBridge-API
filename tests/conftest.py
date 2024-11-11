"""Configuração de testes para a aplicação Flask."""

import os
from sqlite3 import Connection

import pytest
from app.database.session import Base
from app.startup import create_app
from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool


@event.listens_for(Engine, 'connect')
def set_sqlite_pragma(dbapi_connection: Connection, _: None) -> None:
    """Define o pragma de chaves estrangeiras para conexões de banco de dados SQLite.

    Args:
    ----
        dbapi_connection: O objeto de conexão com o banco de dados.
        _: O objeto de registro de conexão (não utilizado).

    """
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()


@pytest.fixture()
def app_testing() -> None:
    """Configura o ambiente de teste para a aplicação Flask.

    - Define o ambiente de teste.
    - Cria a aplicação com configuração de teste e um banco SQLite em memória.
    - Cria as tabelas no banco de dados.
    """
    os.environ["FLASK_ENV"] = "testing"
    app = create_app(TESTING=True, SQLALCHEMY_DATABASE_URI='sqlite:///:memory:')

    with app.app_context():
        engine = create_engine('sqlite:///:memory:', connect_args={"check_same_thread": False}, poolclass=StaticPool)
        Base.metadata.create_all(engine)

    yield app

    with app.app_context():
        Base.metadata.drop_all(engine)


@pytest.fixture()
def client(app_testing: None) -> None:
    """Fornece um cliente de teste para a aplicação Flask."""
    return app_testing.test_client()

@pytest.fixture()
def session() -> None:
    """Contexto de Session para teste de estrutura de banco de dados.

    Yields
    ------
        Session: Uma instancia de Session do SQLAlchemy

    """
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
        echo=True,
    )

    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield session()
    Base.metadata.drop_all(engine)
