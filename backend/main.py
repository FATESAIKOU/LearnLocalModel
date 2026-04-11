from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory database for demonstration purposes
todos = [
    {"id": 1, "task": "Learn React", "completed": False},
    {"id": 2, "task": "Learn Flask", "completed": False}
]
next_id = 3

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    global next_id
    data = request.json
    if not data or 'task' not in data:
        return jsonify({"error": "Task content is required"}), 400
    
    new_todo = {
        "id": next_id,
        "task": data['task'],
        "completed": False
    }
    todos.append(new_todo)
    next_id += 1
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    
    if 'completed' in data:
        todo['completed'] = data['completed']
    if 'task' in data:
        todo['task'] = data['task']
        
    return jsonify(todo)

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({"result": True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
