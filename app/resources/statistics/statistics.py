from app.database.session import get_session
from app.models.club_livro import ClubBook
from sqlalchemy.sql import func

from app.models.review import Review

class StatisticsLogic:
    """Classe com operações de cálculo de estatísticas."""

    @staticmethod
    def average_books_per_club() -> dict:
        """Calcula o número médio de livros lidos por clube."""
        with get_session() as session:
            avg_books = session.query(func.avg(session.query(ClubBook.book_id).filter(ClubBook.club_id == ClubBook.club_id).count())).scalar()
            return {"average_books_per_club": avg_books}

    @staticmethod
    def average_rating_per_book() -> dict:
        """Calcula a média de avaliações dos livros."""
        with get_session() as session:
            avg_rating = session.query(func.avg(Review.rating)).scalar()
            return {"average_rating_per_book": avg_rating}
