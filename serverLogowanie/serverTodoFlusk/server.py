from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import uuid
from notion_client import Client
from pprint import pprint
import json

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

# Notion API
notion_token = 'secret_pGsC4Gut8iMETueuye9fio11NnKpphM3uJf3h6HLihl'
notion_page_id = '908960236f774038bcb4c600e2160462'

def write_text(client, page_id, text, type='paragraph'):
    client.blocks.children.append(
        block_id=page_id,
        children=[{
            "object": "block",
            "type": type,
            type: {
                "rich_text": [{ "type": "text", "text": { "content": text } }]
            }
        }]
    )

def write_dict_to_file_as_json(content, file_name):
    content_as_json_str = json.dumps(content)

    with open(file_name, 'w') as f:
        f.write(content_as_json_str)

def read_text(client, page_id):
    response = client.blocks.children.list(block_id=page_id)
    return response['results']

def create_simple_blocks_from_content(client, content):

    page_simple_blocks = []

    for block in content:

        block_id = block['id']
        block_type = block['type']
        has_children = block['has_children']
        rich_text = block[block_type].get('rich_text')

        if not rich_text:
            return


        simple_block = {
            'id': block_id,
            'type': block_type,
            'text': rich_text[0]['plain_text']
        }

        if has_children:
            nested_children = read_text(client, block_id)
            simple_block['children'] = create_simple_blocks_from_content(client, nested_children)

        page_simple_blocks.append(simple_block)


    return page_simple_blocks

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
