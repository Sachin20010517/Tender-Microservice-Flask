# config.py

import os
from dbConfig.dbConnector import mongodb_config

class Config:
    MONGO_URI = os.getenv("MONGO_URI")  # Ensure MONGO_URI is set in .env file

# Initialize database connection
db = mongodb_config.get_database()
