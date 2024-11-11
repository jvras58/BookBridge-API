"""Arquivos utils para aplicação."""
from flask_restful import abort
from typing import Type
from app.database.session import get_session as Session


def abort_if_record_doesnt_exist(model: Type, record_id: int, session: Session, id_field: str = 'id') -> None:
    """Aborta a requisição se o registro não existir."""
    with Session() as session:
        record = session.query(model).filter(getattr(model, id_field) == record_id).first()
        if not record:
            abort(404, message=f"{model.__name__} {record_id} doesn't exist")

# Exemplo de uso:
# with get_session() as session:
#     abort_if_record_doesnt_exist(TodoModel, todo_id, session)
