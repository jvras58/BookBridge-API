"""Testes para integridade do banco."""

from app.models.todo import TodoItem


def test_create_todo_item(session):
    """Testa a criação de um item TODO no banco de dados."""
    new_todo = TodoItem(task="Teste de tarefa")
    session.add(new_todo)
    session.commit()

    # Verifica se o item foi salvo no banco de dados
    saved_todo = session.query(TodoItem).filter_by(task="Teste de tarefa").first()
    assert saved_todo is not None
    assert saved_todo.task == "Teste de tarefa"


def test_update_todo_item(session):
    """Testa a atualização de um item TODO no banco de dados."""
    todo = TodoItem(task="Tarefa antes da atualização")
    session.add(todo)
    session.commit()

    # Atualiza a tarefa
    todo.task = "Tarefa atualizada"
    session.commit()

    # Verifica se a tarefa foi atualizada
    updated_todo = session.query(TodoItem).filter_by(id=todo.id).first()
    assert updated_todo.task == "Tarefa atualizada"


def test_delete_todo_item(session):
    """Testa a exclusão de um item TODO do banco de dados."""
    todo = TodoItem(task="Tarefa para exclusão")
    session.add(todo)
    session.commit()

    # Exclui o item
    session.delete(todo)
    session.commit()

    # Verifica se o item foi removido
    deleted_todo = session.query(TodoItem).filter_by(task="Tarefa para exclusão").first()
    assert deleted_todo is None


def test_get_todo_item(session):
    """Testa a busca de um item TODO no banco de dados."""
    todo = TodoItem(task="Tarefa para busca")
    session.add(todo)
    session.commit()

    # Busca o item
    fetched_todo = session.query(TodoItem).filter_by(task="Tarefa para busca").first()
    assert fetched_todo is not None
    assert fetched_todo.task == "Tarefa para busca"
