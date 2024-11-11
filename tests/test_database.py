"""Testes para integridade do banco."""

from app.models.user import User
from sqlalchemy import select
from tests.factory.user_factory import UserFactory


def test_create_user(session: None) -> None:
    """Teste de criação de User no banco de dados.

    Args:
    ----
        session (Session): Instancia de Session do SQLAlchemy provisionada pelo Fixture.
    ----

    """
    # GIVEN ------
    # Dada uma Instancia de User com os dados abaixo é salva no banco de dados;
    new_user = UserFactory.build()
    new_user.id = None
    new_user.username = 'user.test'
    session.add(new_user)
    session.commit()

    # WHEN ------
    # Quando executa-se uma busca com um filtro que aponta para o usuário anteriormente
    # salvo;
    user = session.scalar(select(User).where(User.username == 'user.test'))

    # THEN ------
    # Então uma instancia de User é retornada do banco de dados com os mesmos dados que
    # foi salvo anteriormente.
    assert user.username == 'user.test'
    assert user.password_hash == new_user.password_hash

def test_update_user(session: None) -> None:
    """Teste de atualização de User no banco de dados.

    Args:
    ----
        session (Session): Instancia de Session do SQLAlchemy provisionada pelo Fixture.
    ----

    """
    # GIVEN ------
    # Dada uma Instancia de User com os dados abaixo é salva no banco de dados;
    new_user = UserFactory.build()
    new_user.id = None
    new_user.username = 'user.test'
    session.add(new_user)
    session.commit()

    # WHEN ------
    # Quando executa-se uma busca com um filtro que aponta para o usuário anteriormente
    # salvo e atualiza-se o username;
    user = session.scalar(select(User).where(User.username == 'user.test'))
    user.username = 'user.test2'
    session.commit()

    # THEN ------
    # Então uma instancia de User é retornada do banco de dados com o username atualizado.
    assert user.username == 'user.test2'
    assert user.password_hash == new_user.password_hash

def test_delete_user(session: None) -> None:
    """Teste de exclusão de User no banco de dados.

    Args:
    ----
        session (Session): Instancia de Session do SQLAlchemy provisionada pelo Fixture.
    ----

    """
    # GIVEN ------
    # Dada uma Instancia de User com os dados abaixo é salva no banco de dados;
    new_user = UserFactory.build()
    new_user.id = None
    new_user.username = 'user.test'
    session.add(new_user)
    session.commit()

    # WHEN ------
    # Quando executa-se uma busca com um filtro que aponta para o usuário anteriormente
    # salvo e exclui-se o usuário;
    user = session.scalar(select(User).where(User.username == 'user.test'))
    session.delete(user)
    session.commit()

    # THEN ------
    # Então uma instancia de User é retornada do banco de dados com o username atualizado.
    assert session.scalar(select(User).where(User.username == 'user.test')) is None


def test_get_user_by_id(session: None) -> None:
    """Teste de busca de User por ID no banco de dados.

    Args:
    ----
        session (Session): Instancia de Session do SQLAlchemy provisionada pelo Fixture.
    ----

    """
    # GIVEN ------
    # Dada uma Instancia de User com os dados abaixo é salva no banco de dados;
    new_user = UserFactory.build()
    new_user.id = None
    new_user.username = 'user.test'
    session.add(new_user)
    session.commit()

    # WHEN ------
    # Quando executa-se uma busca com um filtro que aponta para o usuário anteriormente
    # salvo e busca-se o usuário pelo ID;
    user = session.scalar(select(User).where(User.username == 'user.test'))
    user_id = user.id
    user = session.scalar(select(User).where(User.id == user_id))

    # THEN ------
    # Então uma instancia de User é retornada do banco de dados com o username atualizado.
    assert user.username == 'user.test'
    assert user.password_hash == new_user.password_hash
    assert user.id == user_id
