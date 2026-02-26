from flask import Blueprint, jsonify, request


bp = Blueprint('todos', __name__)

todos = [
    {
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2026-02-27T18:00:00",
        "created_at": "2026-02-20T14:00:00",
        "updated_at": "2026-02-20T14:00:00"
    }
]

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

@bp.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@bp.route('/todos/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    todo = next((todo for todo in todos if todo['id'] == id), None)
    if todo is not None:
        return jsonify(todo)
    else:
        return jsonify({"error": "Todo not found"}), 404

@bp.route('/todos', methods=['POST'])
def create_todo():
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(new_todo), 201

@bp.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    updated_todo = request.get_json()
    for i, todo in enumerate(todos):
        if todo['id'] == id:
            todos[i] = updated_todo
            return jsonify(updated_todo)
    return jsonify({"error": "Todo not found"}), 404

@bp.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    for i, todo in enumerate(todos):
        if todo['id'] == id:
            deleted_todo = todos.pop(i)
            return jsonify(deleted_todo)
    return jsonify({"error": "Todo not found"}), 404