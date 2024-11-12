"""Módulo para definição das rotas de estatísticas."""

from app.common.swagger import api
from app.resources.statistics.statistics import StatisticsLogic
from flask import Blueprint
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource

statistics_bp = Blueprint("statistics", __name__, url_prefix="/statistics")

statistics_ns = Namespace('statistics', description='Operações de Estatísticas')

api.add_namespace(statistics_ns)

@statistics_ns.route('/average_books_per_club', methods=['GET'])
class AverageBooksPerClubResource(Resource):
    """Recurso para obter a média de livros lidos por clube."""

    @statistics_ns.doc(security='Bearer Auth')
    @jwt_required()
    def get(self) -> dict:
        """Obtém a média de livros lidos por clube."""
        stats = StatisticsLogic.average_books_per_club()
        return stats, 200

@statistics_ns.route('/average_rating_per_book', methods=['GET'])
class AverageRatingPerBookResource(Resource):
    """Recurso para obter a média de avaliações dos livros."""

    @statistics_ns.doc(security='Bearer Auth')
    @jwt_required()
    def get(self) -> dict:
        """Obtém a média de avaliações dos livros."""
        stats = StatisticsLogic.average_rating_per_book()
        return stats, 200
