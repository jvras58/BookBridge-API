"""Contém a lógica das rotas para manipulação de Review."""

from app.database.session import get_session
from app.models.review import Review
from app.models.userbook import UserBook
from flask_jwt_extended import get_jwt_identity


class ReviewLogic:
    """Classe com operações de manipulação de avaliações."""

    @staticmethod
    def create_review(data: dict) -> tuple:
        """Registra uma nova avaliação."""
        book_id = data.get("book_id")
        rating = data.get("rating")
        comment = data.get("comment")
        user_id = get_jwt_identity()
        with get_session() as session:
            user_book = session.query(UserBook).filter_by(user_id=user_id, book_id=book_id).first()
            if not user_book:
                return {"message": "Usuário não leu este livro em nenhum clube"}, 403
            review = Review(book_id=book_id, user_id=user_id, rating=rating, comment=comment)
            session.add(review)
            session.commit()
            return {"message": "Avaliação criada com sucesso"}, 201

    @staticmethod
    def get_reviews_by_book(book_id: int) -> list:
        """Retorna uma lista de todas as avaliações de um livro."""
        with get_session() as session:
            reviews = session.query(Review).filter_by(book_id=book_id).all()
            return [review.to_dict() for review in reviews]
