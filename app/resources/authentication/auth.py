"""Contém a lógica das rotas para manipulação de Auth."""

from datetime import timedelta

from app.database.session import get_session
from app.models.user import User
from flask_jwt_extended import create_access_token


class AuthLogic:
    """Classe com operações de manipulação de auth."""

    @staticmethod
    def authenticate(data: dict) -> tuple:
        """Autentica um usuário e retorna um token JWT."""
        username = data.get("username")
        password = data.get("password")
        with get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            if user and user.check_password(password):
                access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
                return {"access_token": access_token}, 200
            return {"message": "Credenciais inválidas"}, 401
