"""Modulo base para configuração da aplicação."""

from app.common.swagger import init_swagger
from app.config.settings import get_logger, log_response
from app.database.migrate import migrate
from app.database.session import engine
from app.resources.user.user_router import user_bp
from dynaconf import FlaskDynaconf
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager


def create_app(**config: str) -> Flask:
    """Configuração do CORS e carregamento das extensões."""
    app = Flask(__name__)

    FlaskDynaconf(app, settings_files=["settings.toml"])
    app.config.update(config)

    JWTManager(app)
    CORS(app)
    migrate.init_app(app, engine, render_as_batch=True)

    logger = get_logger(app.config['LOG_LEVEL'], app.config['ENVIRONMENT'])
    for rule in app.url_map.iter_rules():
        logger.info("Rota: %s -> Endpoint: %s", rule, rule.endpoint)
    logger.info("Ambiente atual: %s", app.config['ENVIRONMENT'])
    logger.info("Aplicação inicializada com sucesso!")

    app.after_request(log_response)

    # Inicializar Swagger
    init_swagger(app)

    # Registrar blueprints
    app.register_blueprint(user_bp)

    return app
