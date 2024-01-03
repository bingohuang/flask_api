from routes import app
from flask import jsonify, request


@app.route('/students/<student_id>')
def get_student(student_id):
    if request.is_json:
        args = request.get_json()
    student = {'id': student_id, 'name': 'bingo', 'gender': 'male'}

    return jsonify(student)
