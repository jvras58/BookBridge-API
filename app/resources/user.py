"""Contém a lógica das rotas para manipulação de User."""

from flask_jwt_extended import create_access_token
from app.models.user import User
from app.database.session import get_session
from datetime import timedelta

class UserLogic:
    """Classe com operações de manipulação de usuários."""

    @staticmethod
    def register_user(data):
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
    def authenticate_user(data):
        """Autentica um usuário e retorna um token JWT."""
        username = data.get("username")
        password = data.get("password")
        with get_session() as session:
            user = session.query(User).filter_by(username=username).first()
            if user and user.check_password(password):
                access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
                return {"access_token": access_token}, 200
            return {"message": "Credenciais inválidas"}, 401
