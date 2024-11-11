"""Módulo de roteamento de usuários."""
from app.common.swagger import api
from app.resources.user.user import UserLogic
from flask import Blueprint, request

# TODO (jvras): Descomentar as linhas abaixo para habilitar autenticação JWT
# from flask_jwt_extended import jwt_required   # noqa: ERA001
from flask_restx import Namespace, Resource, fields

user_bp = Blueprint("users", __name__, url_prefix="/users")

user_ns = Namespace('users', description='Operações CRUD de Usuário')

user_model = user_ns.model('User', {
    'username': fields.String(required=True, description='Nome do usuário'),
    'password': fields.String(required=True, description='Senha do usuário'),
})

api.add_namespace(user_ns)

@user_ns.route('/create_user', methods=['POST'])
class RegisterResource(Resource):
    """Recurso para registro de usuário."""

    @user_ns.expect(user_model)
    def post(self) -> dict:
        """Registra um novo usuário."""
        data = request.get_json()
        return UserLogic.create_user(data)

@user_ns.route('/', methods=['GET'])
class UserListResource(Resource):
    """Recurso para listar todos os usuários (admin)."""

    # @user_ns.doc(security='Bearer Auth')
    # @jwt_required()
    def get(self) -> dict:
        """Lista todos os usuários."""
        users = UserLogic.get_all_users()
        return {"users": users}, 200

@user_ns.route('/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
class UserResource(Resource):
    """Recurso para operações CRUD em um único usuário."""

    # @user_ns.doc(security='Bearer Auth')
    # @jwt_required()
    def get(self, user_id: int) -> dict:
        """Obtém os detalhes de um usuário específico pelo ID."""
        user = UserLogic.get_user_by_id(user_id)
        if user:
            return user, 200
        return {"message": "Usuário não encontrado"}, 404

    @user_ns.expect(user_model)
    # @user_ns.doc(security='Bearer Auth')
    # @jwt_required()
    def put(self, user_id: int) -> dict:
        """Atualiza as informações de um usuário existente."""
        data = request.get_json()
        response, status = UserLogic.update_user(user_id, data)
        return response, status

    # @user_ns.doc(security='Bearer Auth')
    # @jwt_required()
    def delete(self, user_id: int) -> dict:
        """Exclui um usuário específico pelo ID."""
        response, status = UserLogic.delete_user(user_id)
        return response, status
