"""Contém a lógica das rotas para manipulação de Book."""

from app.database.session import get_session
from app.models.book import Book


class BookLogic:
    """Classe com operações de manipulação de livros."""

    @staticmethod
    def create_book(data: dict) -> tuple:
        """Registra um novo livro."""
        title = data.get("title")
        author = data.get("author")
        with get_session() as session:
            book = Book(title=title, author=author)
            session.add(book)
            session.commit()
            return {"message": "Livro criado com sucesso"}, 201

    @staticmethod
    def get_all_books() -> list:
        """Retorna uma lista de todos os livros."""
        with get_session() as session:
            books = session.query(Book).all()
            return [book.to_dict() for book in books]

    @staticmethod
    def get_book_by_id(book_id: int) -> dict:
        """Retorna um livro específico, ou None se não existir."""
        with get_session() as session:
            book = session.query(Book).get(book_id)
            return book.to_dict() if book else None

    @staticmethod
    def update_book(book_id: int, data: dict) -> dict:
        """Atualiza um livro existente."""
        with get_session() as session:
            book = session.query(Book).get(book_id)
            if not book:
                return {"message": "Livro não encontrado"}, 404
            book.title = data.get("title")
            book.author = data.get("author")
            session.commit()
            return {"message": "Livro atualizado com sucesso"}, 200

    @staticmethod
    def delete_book(book_id: int) -> dict:
        """Exclui um livro específico."""
        with get_session() as session:
            book = session.query(Book).get(book_id)
            if not book:
                return {"message": "Livro não encontrado"}, 404
            session.delete(book)
            session.commit()
            return {"message": "Livro excluído com sucesso"}, 200
