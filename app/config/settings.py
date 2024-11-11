"""Módulo de configurações e logger."""

import logging
from functools import lru_cache
from logging import Logger

import toml
from flask import request
from pydantic_settings import BaseSettings, SettingsConfigDict
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table


class Settings(BaseSettings):
    """Classe que representa as configurações setadas no settings.toml da aplicação."""

    model_config = SettingsConfigDict(
        toml_file='settings.toml',
    )

    DB_URL: str
    LOG_LEVEL: str = 'DEBUG'
    ENVIRONMENT: str = 'development'
    FLASK_ENV: str
    APP_NAME: str
    DEBUG: bool
    CORS_HEADERS: str
    SECRET_KEY: str

    @classmethod
    def from_toml(cls, env: str) -> 'Settings':
        """Carrega as configurações do arquivo settings.toml com base no ambiente."""
        config = toml.load(cls.model_config['toml_file'])
        return cls(**config[env])


def build_logger(log_level: str, environment: str) -> Logger:
    """Constrói o logger com RichHandler."""
    datefmt_str = '[%X]' if environment == 'development' else '[%Y-%m-%d %X]'
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.DEBUG),
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt=datefmt_str,
        handlers=[RichHandler(rich_tracebacks=True)],
    )
    return logging.getLogger()


def get_logger(
    log_level: str = 'DEBUG',
    environment: str = 'development',
) -> Logger:
    """Retorna o logger configurado conforme o nível de log e o ambiente."""
    return build_logger(log_level, environment)


def log_response(response: str) -> object:
    """Middleware para logar as respostas HTTP."""
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Header")
    table.add_column("Value")

    for header, value in response.headers.items():
        table.add_row(header, value)

    console.log(f"[bold green]Request:[/bold green] {request.method} {request.url}")
    console.log(f"[bold green]Status:[/bold green] {response.status}")
    console.log(table)
    return response


@lru_cache
def get_settings() -> Settings:
    """Retorna as configurações setadas no settings.toml com base no ambiente."""
    import os
    env = os.getenv('FLASK_ENV', 'default')
    return Settings.from_toml(env)
