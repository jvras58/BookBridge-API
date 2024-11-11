"""Configuração de testes para a aplicação Flask."""

from flask import json
import os
from sqlite3 import Connection

import pytest
from app.database.session import Base, engine
from app.startup import create_app
from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import sessionmaker
from app.models.user import User
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
def app_testing():
    """
    Configura o ambiente de teste para a aplicação.

    Define a variável de ambiente 'FLASK_ENV' como 'testing'.
    Cria uma instância da aplicação usando a função 'create_app_wsgi()'.
    Cria o banco de dados usando o contexto da aplicação.
    Retorna a instância da aplicação.
    Ao finalizar o teste, remove o banco de dados.

    Returns:
        app: Instância da aplicação configurada para teste.
    """
    os.environ["FLASK_ENV"] = "testing"
    app = create_app()
    with app.app_context():
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

@pytest.fixture()
def new_user() -> dict:
    """Cria um novo usuário para testes."""
    return {
        "username": "testuser",
        "password": "testpassword"
    }

@pytest.fixture()
def create_new_user(session: None, new_user: dict) -> None:
    """Cria um novo usuário no banco de dados para testes."""
    user = User(username=new_user['username'])
    user.set_password(new_user['password'])
    session.add(user)
    session.commit()
    return user

@pytest.fixture()
def create_new_user_api(client, new_user) -> dict:
    """Cria um novo usuário usando a rota da API e retorna os dados."""
    response = client.post('/users/create_user', data=json.dumps(new_user), content_type='application/json')
    assert response.status_code == 201
    return response.json
