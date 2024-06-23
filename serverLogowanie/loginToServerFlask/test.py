from pymongo import MongoClient

# Create a MongoClient object and specify the connection URL
client = MongoClient("mongodb://admin:password@localhost:27017/")
print(client.server_info())

# Access a specific database
db = client["users"]

# Access a specific collection within the database
collection = db["user"]

# Perform operations on the collection
# For example, insert a document
document = {"email": "John", "password": "1232"}
collection.insert_one(document)

# Close the connection
client.close()
