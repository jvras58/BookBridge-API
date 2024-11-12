"""Contém a lógica das rotas para manipulação de Club."""

from app.database.session import get_session
from app.models.book import Book
from app.models.club import Club
from app.models.club_livro import ClubBook


class ClubLogic:
    """Classe com operações de manipulação de clubes."""

    @staticmethod
    def create_club(data: dict) -> tuple:
        """Registra um novo clube."""
        name = data.get("name")
        with get_session() as session:
            if session.query(Club).filter_by(name=name).first():
                return {"message": "Clube já existe"}, 409
            club = Club(name=name)
            session.add(club)
            session.commit()
            return {"message": "Clube criado com sucesso"}, 201

    @staticmethod
    def add_book_to_club(club_id: int, book_id: int) -> dict:
        """Adiciona um livro a um clube."""
        with get_session() as session:
            if not session.query(Club).get(club_id):
                return {"message": "Clube não encontrado"}, 404
            if not session.query(Book).get(book_id):
                return {"message": "Livro não encontrado"}, 404
            club_book = ClubBook(club_id=club_id, book_id=book_id)
            session.add(club_book)
            session.commit()
            return {"message": "Livro adicionado ao clube com sucesso"}, 200

    @staticmethod
    def get_books_of_club(club_id: int) -> list:
        """Retorna uma lista de todos os livros de um clube."""
        with get_session() as session:
            books = session.query(Book).join(ClubBook).filter(ClubBook.club_id == club_id).all()
            return [book.to_dict() for book in books]

    @staticmethod
    def remove_book_from_club(club_id: int, book_id: int) -> dict:
        """Remove um livro de um clube."""
        with get_session() as session:
            club_book = session.query(ClubBook).filter_by(club_id=club_id, book_id=book_id).first()
            if not club_book:
                return {"message": "Associação entre clube e livro não encontrada"}, 404
            session.delete(club_book)
            session.commit()
            return {"message": "Livro removido do clube com sucesso"}, 200
