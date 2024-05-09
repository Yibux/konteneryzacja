from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import flask
import enum
import uuid
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Enum('TODO', 'IN_PROGRESS', 'DONE'), nullable=False)
    due_date = db.Column(db.Date)

class TaskRequest:
    def __init__(self, name, status, due_date):
        self.name = name
        self.status = status
        self.due_date = due_date

@app.route('/api/all', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()
    serialized_tasks = [
        {
            'id': task.id,
            'name': task.name,
            'status': task.status,
            'dueDate': task.due_date.strftime('%Y-%m-%d') if task.due_date else None
        }
        for task in tasks
    ]
    return jsonify(serialized_tasks)

@app.route('/api/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if task:
        serialized_task = {
            'id': task.id,
            'name': task.name,
            'status': task.status,
            'dueDate': task.due_date.strftime('%Y-%m-%d') if task.due_date else None
        }
        return jsonify(serialized_task)
    else:
        return jsonify({"message": "Task not found"}), 400

@app.route('/api/add', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(
        id=str(uuid.uuid4()),
        name=data['name'],
        status=data['status'],
        due_date=data['dueDate'] if 'dueDate' in data else None
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added successfully"})

@app.route('/api/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    if task:
        data = request.get_json()
        task.name = data['name']
        task.status = data['status']
        task.due_date = data['dueDate'] if 'dueDate' in data else None
        db.session.commit()
        return jsonify({"message": "Task updated successfully"})
    else:
        return jsonify({"message": "Task not found"}), 400

@app.route('/api/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully"})
    else:
        return jsonify({"message": "Task not found"}), 400

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
