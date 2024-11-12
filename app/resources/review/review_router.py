"""Módulo de roteamento de avaliações."""
from app.common.swagger import api
from app.resources.review.review import ReviewLogic
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

review_bp = Blueprint("reviews", __name__, url_prefix="/reviews")

review_ns = Namespace('reviews', description='Operações CRUD de Avaliação')

review_model = review_ns.model('Review', {
    'book_id': fields.Integer(required=True, description='ID do livro'),
    'rating': fields.Integer(required=True, description='Avaliação do livro', min=0, max=5),
    'comment': fields.String(description='Comentário sobre o livro'),
})

api.add_namespace(review_ns)

@review_ns.route('/create_review', methods=['POST'])
class RegisterReviewResource(Resource):
    """Recurso para registro de avaliação."""

    @review_ns.doc(security='Bearer Auth')
    @jwt_required()
    @review_ns.expect(review_model)
    def post(self) -> dict:
        """Registra uma nova avaliação."""
        data = request.get_json()
        return ReviewLogic.create_review(data)

@review_ns.route('/<int:book_id>', methods=['GET'])
class BookReviewsResource(Resource):
    """Recurso para listar todas as avaliações de um livro."""

    @review_ns.doc(security='Bearer Auth')
    @jwt_required()
    def get(self, book_id: int) -> dict:
        """Lista todas as avaliações de um livro."""
        reviews = ReviewLogic.get_reviews_by_book(book_id)
        return {"reviews": reviews}, 200
