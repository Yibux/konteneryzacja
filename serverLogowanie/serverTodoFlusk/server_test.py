# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# import uuid
# from notion_client import Client
import os
import mysql.connector
# app = Flask(__name__)
# CORS(app)
# Get the DATABASE_USER from environment variable
database_user = os.environ.get('DATABASE_USER')
database_port = os.environ.get('DATABASE_PORT')
database_name = os.environ.get('DATABASE_NAME')
database_host = os.environ.get('DATABASE_HOST')
database_password = os.environ.get('DATABASE_PASSWORD')

# database_user = 'root'
# database_port = '3306'
# database_name = 'db'
# database_host = 'mysql'
# database_password = 'root'

print(str(database_user) + ' ' + str(database_port) + ' ' + str(database_name) + ' ' + str(database_host), ' ' + str(database_password))

# Use the DATABASE_USER in your code
# app.config['SQLALCHEMY_DATABASE_URI'] = f'''
#     {database_host}://{database_user}:{database_root_password}@{database_name}:{database_port}/{database_name}
#     '''

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db:3306/db'


# Create a connection to MySQL
cnx = mysql.connector.connect(
    user=str(database_user),
    password=str(database_password),
    host=str(database_host),
    port=str(database_port),
    database=str(database_name)
)

# cnx = mysql.connector.connect(
#     user='root',
#     password='root',
#     host='localhost',
#     port='3306',
#     database='db'
# )

# Check if the connection is successful
if cnx.is_connected():
    print("Connected to MySQL database")
else:
    print("Connection failed")

# Close the connection
cnx.close()

# print("connection works")