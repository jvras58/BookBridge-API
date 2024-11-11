"""Contém a lógica das rotas para manipulação dos itens TODO."""
from app.common.utils import abort_if_todo_doesnt_exist, parser
from app.database.session import get_session
from app.models.todo import TodoItem as TodoModel


class Todo:
    """Lógica de manipulação de um único item TODO."""

    def get(self, todo_id: int) -> dict:
        """Obtém um item TODO."""
        with get_session() as session:
            todo = session.query(TodoModel).filter_by(id=todo_id).first()
            if not todo:
                abort_if_todo_doesnt_exist(todo_id)
            return {'task': todo.task}

    def delete(self, todo_id: int) -> dict:
        """Remove um item TODO."""
        with get_session() as session:
            todo = session.query(TodoModel).filter_by(id=todo_id).first()
            if not todo:
                abort_if_todo_doesnt_exist(todo_id)
            session.delete(todo)
            session.commit()
            return '', 204

    def put(self, todo_id: int) -> dict:
        """Atualiza um item TODO."""
        args = parser.parse_args()
        with get_session() as session:
            todo = session.query(TodoModel).filter_by(id=todo_id).first()
            if not todo:
                abort_if_todo_doesnt_exist(todo_id)
            todo.task = args['task']
            session.commit()
            return {'task': todo.task}, 200


class TodoList:
    """Lógica de manipulação da lista de itens TODO."""

    def get(self) -> dict:
        """Obtém a lista de itens TODO."""
        with get_session() as session:
            todos = session.query(TodoModel).all()
            return {f'todo{todo.id}': {'task': todo.task} for todo in todos}

    def post(self) -> dict:
        """Adiciona um novo item TODO."""
        args = parser.parse_args()
        with get_session() as session:
            todo = TodoModel(task=args['task'])
            session.add(todo)
            session.commit()
            return {'task': todo.task}, 201
