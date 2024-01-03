from flask_restful import Resource
from resources import api
from services.book_service import BookService


class BookResource(Resource):
    def get(self, book_id: int):
        book_model = BookService().get_book_by_id(book_id)
        if book_model:
            return book_model.serialize()
        else:
            return {'error': f'Book[{book_id}] not found'}, 404

    def put(self, student_id: int):
        return {'id': student_id, 'name': 'Bingo', 'gender': 'male'}


api.add_resource(BookResource, '/books/<int:book_id>')
