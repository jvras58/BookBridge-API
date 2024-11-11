"""Arquivos utils para aplicação."""
from flask_restful import abort, reqparse
from app.database.session import get_session
from app.models.todo import TodoItem as TodoModel

parser = reqparse.RequestParser()
parser.add_argument('task')

def abort_if_todo_doesnt_exist(todo_id: int) -> None:
    """Aborta a requisição se o item TODO não existir."""
    with get_session() as session:
        todo = session.query(TodoModel).filter_by(id=todo_id).first()
        if not todo:
            abort(404, message=f"Todo {todo_id} doesn't exist")
