from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import uuid
from notion_client import Client

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

notion_token = 'secret_frHHTxg46cnG0Hwqaa18G45RcARsUrccAzpKPPs6VU2'
notion_page_id = 'ecde2dd21cfc4ed29ca7a807b0110203'
notion_database_id = 'fa7e2a2f5d5349cf9f47caaba2607d8f'
client = Client(auth=notion_token)

app.app_context().push()
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Enum('TODO', 'IN_PROGRESS', 'DONE'), nullable=False)
    due_date = db.Column(db.Date)
    owner = db.Column(db.String(100), nullable=False)

class TaskRequest:
    def __init__(self, name, status, due_date, owner):
        self.name = name
        self.status = status
        self.due_date = due_date
        self.owner = owner

@app.route('/api/all/<id>', methods=['GET'])
def get_all_tasks_by_id(id):
    tasks = Task.query.filter_by(owner=id).all()
    serialized_tasks = [
        {
            'id': task.id,
            'name': task.name,
            'status': task.status,
            'dueDate': task.due_date.strftime('%Y-%m-%d') if task.due_date else None,
            'owner': task.owner
        }
        for task in tasks
    ]
    return jsonify(serialized_tasks)

@app.route('/api/all', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()
    serialized_tasks = [
        {
            'id': task.id,
            'name': task.name,
            'status': task.status,
            'dueDate': task.due_date.strftime('%Y-%m-%d') if task.due_date else None,
            'owner': task.owner
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
            'dueDate': task.due_date.strftime('%Y-%m-%d') if task.due_date else None,
            'owner': task.owner
        }
        return jsonify(serialized_task)
    else:
        return jsonify({"message": "Task not found"}), 400

@app.route('/api/add/<id>', methods=['POST'])
def add_task(id):
    data = request.get_json()
    new_task = Task(
        id=str(uuid.uuid4()),
        name=data['name'],
        status=data['status'],
        due_date=data['dueDate'] if 'dueDate' in data else None,
        owner=id
    )
    db.session.add(new_task)
    db.session.commit()
    write_row(client, notion_database_id, data['status'], data['dueDate'], data['name'], id)
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
        # update_row(client, notion_database_id, data['status'], data['dueDate'], data['name'], task.owner)
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

def write_row(client, database_id, status, date, name, owner):

    client.pages.create(
        **{
            "parent": {
                "database_id": database_id
            },
            'properties': {
                'status': {'multi_select': [{'name': status}]},
                'owner': {'rich_text': [{'text': {'content': owner}}]},
                'due_date': {'date': {'start': date}},
                'name': {'title': [{'text': {'content': name}}]},
            }
        }
    )
    
def update_row(client, database_id, status, due_date, name, owner):
    
        db_rows = client.databases.query(database_id=database_id)
    
        for row in db_rows['results']:
            if safe_get(row, 'properties.name.title.0.text.content') == name:
                row_id = row['id']
                break
    
        client.pages.update(
            **{
                "page_id": row_id,
                'properties': {
                    'status': {'multi_select': [{'name': status}]},
                    'owner': {'rich_text': [{'text': {'content': owner}}]},
                    'due_date': {'date': {'start': due_date}},
                    'name': {'title': [{'text': {'content': name}}]},
                }
            }
        )

def safe_get(data, dot_chained_keys):
    '''
        {'a': {'b': [{'c': 1}]}}
        safe_get(data, 'a.b.0.c') -> 1
    '''
    keys = dot_chained_keys.split('.')
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except (KeyError, TypeError, IndexError):
            return None
    return data

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
