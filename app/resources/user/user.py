"""Contém a lógica das rotas para manipulação de User."""

from app.database.session import get_session
from app.models.user import User


class UserLogic:
    """Classe com operações de manipulação de usuários."""

    @staticmethod
    def create_user(data: dict) -> tuple:
        """Registra um novo usuário."""
        username = data.get("username")
        password = data.get("password")
        with get_session() as session:
            if session.query(User).filter_by(username=username).first():
                return {"message": "Usuário já existe"}, 409
            user = User(username=username)
            user.set_password(password)
            session.add(user)
            session.commit()
            return {"message": "Usuário criado com sucesso"}, 201

    @staticmethod
    def get_all_users() -> list:
        """Retorna uma lista de todos os usuários."""
        with get_session() as session:
            users = session.query(User).all()
            return [user.to_dict() for user in users]

    @staticmethod
    def get_user_by_id(user_id: int) -> dict:
        """Retorna um usuário específico, ou None se não existir."""
        with get_session() as session:
            user = session.query(User).get(user_id)
            return user.to_dict() if user else None

    @staticmethod
    def update_user(user_id: int, data: dict) -> dict:
        """Atualiza um usuário existente."""
        with get_session() as session:
            user = session.query(User).get(user_id)
            if not user:
                return {"message": "Usuário não encontrado"}, 404
            user.username = data.get("username")
            user.set_password(data.get("password"))
            session.commit()
            return {"message": "Usuário atualizado com sucesso"}, 200

    @staticmethod
    def delete_user(user_id: int) -> dict:
        """Exclui um usuário específico."""
        with get_session() as session:
            user = session.query(User).get(user_id)
            if not user:
                return {"message": "Usuário não encontrado"}, 404
            session.delete(user)
            session.commit()
            return {"message": "Usuário excluído com sucesso"}, 200
