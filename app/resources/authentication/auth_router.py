"""Modulo que define o Blueprint para o resources `login/register` para as rotas."""
from app.common.swagger import api
from app.resources.authentication.auth import AuthLogic
from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

auth_ns = Namespace('auth', description='Operações de autenticação')

auth_model = auth_ns.model('User', {
    'username': fields.String(required=True, description='Nome do usuário'),
    'password': fields.String(required=True, description='Senha do usuário'),
})


@auth_ns.route('/login', methods=['POST'])
class LoginResource(Resource):
    """Recurso para autenticação de usuário."""

    @auth_ns.expect(auth_model)
    def post(self) -> dict:
        """Autentica o usuário e retorna um token JWT."""
        data = request.get_json()
        return AuthLogic.authenticate(data)

api.add_namespace(auth_ns)
