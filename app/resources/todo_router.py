"""Módulo responsável por definir as rotas relacionadas aos TODOs."""

from flask import Blueprint
from flask_restx import Namespace, Resource, fields

from app.common.swagger import api
from app.resources.todo import Todo, TodoList

todo_bp = Blueprint('todos', __name__, url_prefix='/todos')

todo_ns = Namespace('tasks', path='', description='Operações relacionadas aos TODOs')

todo_model = todo_ns.model('Todo', {
    'task': fields.String(required=True, description='Descrição da tarefa'),
})

todo_logic = Todo()
todo_list_logic = TodoList()

@todo_ns.route('/')
class TodoListResource(Resource):
    """Operações relacionadas a criação e listagem de TODOs."""

    def get(self) -> list:
        """Obtém a lista de TODOs."""
        return todo_list_logic.get()

    @todo_ns.expect(todo_model)
    @todo_ns.marshal_with(todo_model, code=201)
    def post(self) -> dict:
        """Cria um novo TODO."""
        return todo_list_logic.post()

@todo_ns.route('/<string:todo_id>')
class TodoResource(Resource):
    """Operações relacionadas a um TODO específico."""

    @todo_ns.marshal_with(todo_model)
    def get(self, todo_id: str) -> dict:
        """Obtém um TODO específico."""
        return todo_logic.get(todo_id)

    def delete(self, todo_id: str) -> dict:
        """Remove um TODO."""
        return todo_logic.delete(todo_id)

    @todo_ns.expect(todo_model)
    @todo_ns.marshal_with(todo_model)
    def put(self, todo_id: str) -> dict:
        """Atualiza um TODO."""
        return todo_logic.put(todo_id)

api.add_namespace(todo_ns)
