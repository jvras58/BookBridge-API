"""Documentação do Swagger."""

from flask_restx import Api
from flask import request


class CustomApi(Api):
    """Classe customizada para incluir 'Bearer ' automaticamente no token JWT."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def headers(self):
        headers = super().headers
        auth_header = request.headers.get("Authorization", "")
        
        # Se o token não tiver 'Bearer ', adicione-o automaticamente
        if auth_header and not auth_header.startswith("Bearer "):
            headers["Authorization"] = f"Bearer {auth_header}"

        return headers

api = Api(
    version='1.0',
    title='API - BookBridge',
    description='Uma API simples de gerenciamento de clubes de leitura',
    doc='/docs',
    security='Bearer Auth',
    authorizations={
    'Bearer Auth': {
    'type': 'apiKey',
    'in': 'header',
    'name': 'Authorization',
    'description': 'Token JWT usando o formato: Bearer <access_token>',
            }
        }
    )

def init_swagger(app):
    api.init_app(app)
