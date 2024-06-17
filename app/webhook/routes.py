import os
import sys
from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import datetime
import logging

webhook = Blueprint('webhook', __name__)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import conn_string

# Set up MongoDB connection
client = MongoClient(conn_string)
db = client['github']
collection = db['status']

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@webhook.route('/webhook/receiver', methods=['POST'])
def webhook_receiver():
    data = request.json
    #print("Received data:", data)  

    logger.debug(f"Received data: {data}")

    if 'action' not in data:
        logger.error("Missing required fields")
        return jsonify({"error": "Missing required fields"}), 400
    
    collection.insert_one(data)
    return jsonify({"status": "success"}), 200


