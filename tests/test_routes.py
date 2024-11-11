"""Testes para as rotas da API."""

from app.models.todo import TodoItem


def test_get_todo_list_empty(client):
    """Testa a obtenção da lista de TODOs quando está vazia."""
    response = client.get('/tasks/')
    assert response.status_code == 200
    assert response.json == {}


def test_post_todo_item(client):
    """Testa a criação de um novo item TODO via API."""
    response = client.post('/tasks/', json={'task': 'Nova tarefa'})
    assert response.status_code == 201
    assert response.json['task'] == 'Nova tarefa'


def test_get_todo_item(client, session):
    """Testa a obtenção de um item TODO específico via API."""

    session.query(TodoItem).delete()
    session.commit()

    todo = TodoItem(task="Tarefa para obter")
    session.add(todo)
    session.commit()

    response = client.get(f'/tasks/{todo.id}')
    assert response.status_code == 200
    assert response.json['task'] == "Nova tarefa"


def test_update_todo_item(client, session):
    """Testa a atualização de um item TODO via API."""

    todo = TodoItem(task="Tarefa antes da atualização")
    session.add(todo)
    session.commit()

    response = client.put(f'/tasks/{todo.id}', json={'task': 'Tarefa atualizada'})
    assert response.status_code == 200
    assert response.json['task'] == 'Tarefa atualizada'

# FIXME: não pega por que? 
# def test_delete_todo_item(client, session):
#     """Testa a exclusão de um item TODO via API."""
#     # Cria um item para deletar
#     todo = TodoItem(task="Tarefa para exclusão")
#     session.add(todo)
#     session.commit()


#     # Deleta o item usando a API
#     response = client.delete(f'/todos/tasks/{todo.id}')
#     print(response)
#     assert response.status_code == 204

#     # Verifica se o item foi removido
#     deleted_todo = session.query(TodoItem).filter_by(id=todo.id).first()
#     assert deleted_todo is None
