from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)
CORS(app)

# MongoDB configuration

# authentication_database = 'admin'
# username = 'admin'
# password = 'password'
# database = 'users'
# host = 'localhost'
# port = int('27017')

username = os.environ.get('DATABASE_USER')
password = os.environ.get('DATABASE_PASSWORD')
host = os.environ.get('DATABASE_HOST')
port = os.environ.get('DATABASE_PORT')
db_name = os.environ.get('DATABASE_NAME')


# client = MongoClient(host, int(port), username=username, password=password, authSource = authentication_database)
connection_string = f'mongodb://{username}:{password}@{host}:{port}/'
print(connection_string)
client = MongoClient(f"mongodb://{username}:{password}@{host}:27017/")
# client = MongoClient("mongodb://admin:password@localhost:27017/")
print(client)
print(client.server_info())
# try:
#     print(client.list_database_names())
# except Exception as e:
#     print(f"Error: {e}")

db = client['users']
user_collection = db['user']

# Helper functions
def user_to_dict(user):
    return {
        "id": str(user["_id"]),
        "username": user.get("username"),
        "email": user.get("email"),
        "password": user.get("password")
    }

@app.route('/server/status', methods=['GET'])
def check_server_status():
    try:
        client.server_info()
        return jsonify({"message": "Server is connected"}), 200
    except Exception as e:
        return jsonify({"message": "Server is not connected", "error": str(e)}), 500

@app.route('/user/all', methods=['GET'])
def get_all_users():
    users = list(user_collection.find())
    return jsonify([user_to_dict(user) for user in users]), 200

@app.route('/user/add', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = {
        "username": None,
        "email": data['email'],
        "password": data['password']
    }

    if user_collection.find_one({"email": new_user['email']}):
        return jsonify({"message": "User already exists"}), 400

    user_collection.insert_one(new_user)
    return jsonify(user_to_dict(new_user)), 200

@app.route('/user/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user = user_collection.find_one({"email": email, "password": password})
    if user:
        return jsonify(user_to_dict(user)), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
