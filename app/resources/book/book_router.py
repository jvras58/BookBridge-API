"""Módulo de roteamento de livros."""
from app.common.swagger import api
from app.resources.book.book import BookLogic
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

book_bp = Blueprint("books", __name__, url_prefix="/books")

book_ns = Namespace('books', description='Operações CRUD de Livro')

book_model = book_ns.model('Book', {
    'title': fields.String(required=True, description='Título do livro'),
    'author': fields.String(required=True, description='Autor do livro'),
})

api.add_namespace(book_ns)

@book_ns.route('/create_book', methods=['POST'])
class RegisterBookResource(Resource):
    """Recurso para registro de livro."""

    @book_ns.doc(security='Bearer Auth')
    @jwt_required()
    @book_ns.expect(book_model)
    def post(self) -> dict:
        """Registra um novo livro."""
        data = request.get_json()
        return BookLogic.create_book(data)

@book_ns.route('/', methods=['GET'])
class BookListResource(Resource):
    """Recurso para listar todos os livros."""

    @book_ns.doc(security='Bearer Auth')
    @jwt_required()
    def get(self) -> dict:
        """Lista todos os livros."""
        books = BookLogic.get_all_books()
        return {"books": books}, 200

@book_ns.route('/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
class BookResource(Resource):
    """Recurso para operações CRUD em um único livro."""

    @book_ns.doc(security='Bearer Auth')
    @jwt_required()
    def get(self, book_id: int) -> dict:
        """Obtém os detalhes de um livro específico pelo ID."""
        book = BookLogic.get_book_by_id(book_id)
        if book:
            return book, 200
        return {"message": "Livro não encontrado"}, 404

    @book_ns.doc(security='Bearer Auth')
    @jwt_required()
    @book_ns.expect(book_model)
    def put(self, book_id: int) -> dict:
        """Atualiza as informações de um livro existente."""
        data = request.get_json()
        response, status = BookLogic.update_book(book_id, data)
        return response, status

    @book_ns.doc(security='Bearer Auth')
    @jwt_required()
    def delete(self, book_id: int) -> dict:
        """Exclui um livro específico pelo ID."""
        response, status = BookLogic.delete_book(book_id)
        return response, status
