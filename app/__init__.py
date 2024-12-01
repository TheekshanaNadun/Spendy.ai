from flask import Flask
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["spendy_ai"]

# Import routes
from app import routes
