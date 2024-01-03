from flask_restful import Resource
from resources import api


class StudentResource(Resource):
    def get(self, student_id: int):
        if student_id == 1:
            return {'id': student_id, 'name': 'Bingo', 'gender': 'male'}
        else:
            return {'error': f'student[{student_id}] not found'}, 404

    def put(self, student_id: int):
        return {'id': student_id, 'name': 'Bingo', 'gender': 'male'}


api.add_resource(StudentResource, '/students/<int:book_id>')
