"""Documentação do Swagger."""

from flask_restx import Api

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
            },
        },
    )

def init_swagger(app: object) -> None:
    """Inicializa a documentação do Swagger."""
    api.init_app(app)
