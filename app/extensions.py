from pymongo import MongoClient
from config import conn_string

def mongo(data):
    try:
        client = MongoClient(conn_string)
        db = client['github']
        collection = db['status']
        result = collection.insert_one(data)
        print(f"Data inserted with id: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example data to insert
data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

mongo(data)
