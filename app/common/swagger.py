"""Documentação do Swagger."""

from flask_restx import Api

api = Api(
    version='1.0',
    title='API - semple',
    description='Uma API simples',
    doc='/docs'
)

def init_swagger(app):
    api.init_app(app)
