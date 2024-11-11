"""Modulo que define o Blueprint para o resources `USER` para as rotas."""



from flask import Blueprint, request
from flask_restx import Resource, fields, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.resources.user import UserLogic
from app.common.swagger import api

user_bp = Blueprint("users", __name__, url_prefix="/users")

user_ns = Namespace('users', description='Operações relacionadas a Usuários')

user_model = user_ns.model('User', {
    'username': fields.String(required=True, description='Nome do usuário'),
    'password': fields.String(required=True, description='Senha do usuário')
})

@user_ns.route('/register')
class UserRegisterResource(Resource):
    """Recurso para registro de usuário."""

    @user_ns.expect(user_model)
    def post(self):
        """Cria um novo usuário."""
        data = request.get_json()
        return UserLogic.register_user(data)

@user_ns.route('/login')
class UserLoginResource(Resource):
    """Recurso para autenticação de usuário."""

    @user_ns.expect(user_model)
    def post(self):
        """Autentica o usuário e retorna um token JWT."""
        data = request.get_json()
        return UserLogic.authenticate_user(data)

@user_ns.route('/protected')
class ProtectedResource(Resource):
    """Exemplo de rota protegida com JWT."""

    @jwt_required()
    def get(self):
        """Retorna informações de um usuário autenticado."""
        current_user = get_jwt_identity()
        return {"message": f"Bem-vindo, usuário {current_user}!"}

api.add_namespace(user_ns)
