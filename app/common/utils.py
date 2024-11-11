"""Arquivos utils para aplicação."""
from __future__ import annotations

from typing import TYPE_CHECKING

from flask_restful import abort

if TYPE_CHECKING:
    from app.database.session import get_session


def abort_if_record_doesnt_exist(model: type, record_id: int, session: get_session, id_field: str = 'id') -> None:
    """Aborta a requisição se o registro não existir."""
    with session() as local_session:
        record = local_session.query(model).filter(getattr(model, id_field) == record_id).first()
        if not record:
            abort(404, message=f"{model.__name__} {record_id} doesn't exist")

# Exemplo de uso:
# with get_session() as session:
#     abort_if_record_doesnt_exist(USer, user_id, session)  # noqa: ERA001
