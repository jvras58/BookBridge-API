"""Documentação do Swagger."""

from flask_restx import Api

api = Api(
    version='1.0',
    title='API - BookBridge',
    description='Uma API simples de gerenciamento de clubes de leitura',
    doc='/docs'
)

def init_swagger(app):
    api.init_app(app)
