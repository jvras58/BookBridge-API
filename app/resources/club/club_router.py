"""Módulo de roteamento de clubes."""
from app.common.swagger import api
from app.resources.club.club import ClubLogic
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

club_bp = Blueprint("clubs", __name__, url_prefix="/clubs")

club_ns = Namespace('clubs', description='Operações CRUD de Clube')

club_model = club_ns.model('Club', {
    'name': fields.String(required=True, description='Nome do clube'),
})

add_book_club_model = club_ns.model('AddBook', {
    'club_id': fields.Integer(required=True, description='ID do clube'),
    'book_id': fields.Integer(required=True, description='ID do livro'),
})

add_user_book_model = club_ns.model('AddUserBook', {
    'club_id': fields.Integer(required=True, description='ID do clube'),
    'book_id': fields.Integer(required=True, description='ID do livro'),
    'user_id': fields.Integer(required=True, description='ID do usuário'),
})

api.add_namespace(club_ns)

@club_ns.route('/create_club', methods=['POST'])
class RegisterClubResource(Resource):
    """Recurso para registro de clube."""

    @club_ns.doc(security='Bearer Auth')
    @jwt_required()
    @club_ns.expect(club_model)
    def post(self) -> dict:
        """Registra um novo clube."""
        data = request.get_json()
        return ClubLogic.create_club(data)

@club_ns.route('/<int:club_id>/book', methods=['POST'])
class AddBookToClubResource(Resource):
    """Recurso para adicionar um livro a um clube."""

    @club_ns.doc(security='Bearer Auth')
    @jwt_required()
    @club_ns.expect(add_book_club_model)
    def post(self, club_id: int) -> dict:
        """Adiciona um livro a um clube."""
        data = request.get_json()
        book_id = data.get("book_id")
        return ClubLogic.add_book_to_club(club_id, book_id)

@club_ns.route('/<int:club_id>/user_book', methods=['POST'])
class AddUserBookToClubResource(Resource):
    """Recurso para adicionar um livro lido por um usuário a um clube."""

    @club_ns.doc(security='Bearer Auth')
    @jwt_required()
    @club_ns.expect(add_user_book_model)
    def post(self, club_id: int) -> dict:
        """Adiciona um livro lido por um usuário a um clube."""
        data = request.get_json()
        book_id = data.get("book_id")
        user_id = data.get("user_id")
        return ClubLogic.add_user_book(club_id, book_id, user_id)

@club_ns.route('/<int:club_id>/books', methods=['GET'])
class ClubBooksResource(Resource):
    """Recurso para listar todos os livros de um clube."""

    @club_ns.doc(security='Bearer Auth')
    @jwt_required()
    def get(self, club_id: int) -> dict:
        """Lista todos os livros de um clube."""
        books = ClubLogic.get_books_of_club(club_id)
        return {"books": books}, 200

@club_ns.route('/<int:club_id>/books/<int:book_id>', methods=['DELETE'])
class RemoveBookFromClubResource(Resource):
    """Recurso para remover um livro de um clube."""

    @club_ns.doc(security='Bearer Auth')
    @jwt_required()
    def delete(self, club_id: int, book_id: int) -> dict:
        """Remove um livro de um clube."""
        return ClubLogic.remove_book_from_club(club_id, book_id)
