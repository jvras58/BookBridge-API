import json

"""Testes para as rotas da API."""


def test_create_user(client, new_user):
    """Teste para criação de um novo usuário."""
    response = client.post('/users/create_user', data=json.dumps(new_user), content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == 'Usuário criado com sucesso'

def test_get_all_users(client):
    """Teste para listar todos os usuários."""
    response = client.get('/users/')
    assert response.status_code == 200
    assert 'users' in response.json

def test_get_user_by_id(client, new_user):
    """Teste para obter um usuário específico pelo ID."""
    # Primeiro, cria um novo usuário (criar uma fixture para isso)
    create_response = client.post('/users/create_user', data=json.dumps(new_user), content_type='application/json')
    # Em seguida, obtém o usuário pelo ID
    response = client.get(f'/users/1')
    assert response.status_code == 200
    assert response.json['username'] == new_user['username']

def test_update_user(client, new_user):
    """Teste para atualizar as informações de um usuário existente."""
    # Dados atualizados do usuário
    create_response = client.post('/users/create_user', data=json.dumps(new_user), content_type='application/json')
    assert create_response.status_code == 201
    updated_user = {
        "username": "updateduser",
        "password": "updatedpassword"
    }

    # Em seguida, atualiza o usuário pelo ID
    response = client.put(f'/users/1', data=json.dumps(updated_user), content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == 'Usuário atualizado com sucesso'

def test_delete_user(client, new_user):
    """Teste para excluir um usuário específico pelo ID."""
    # Primeiro, cria um novo usuário
    create_response = client.post('/users/create_user', data=json.dumps(new_user), content_type='application/json')

    # Em seguida, exclui o usuário pelo ID
    response = client.delete(f'/users/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Usuário excluído com sucesso'

    # Verifica se o usuário foi realmente excluído
    get_response = client.get(f'/users/1')
    assert get_response.status_code == 404
    assert get_response.json['message'] == "Usuário não encontrado"
