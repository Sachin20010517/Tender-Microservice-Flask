from pymongo import MongoClient
from dotenv import load_dotenv
import os
import logging

load_dotenv()  # Load environment variables from .env file

class MongoDBConfig:
    def __init__(self):
        self.DATABASE_URL = os.getenv("MONGO_URI")
        self.DATABASE_NAME = os.getenv("DATABASE_NAME")
        self.client = None
        self.database = None

    def connect_to_mongo(self):
        try:
            logging.info("Connecting to MongoDB...")
            self.client = MongoClient(self.DATABASE_URL)
            self.database = self.client[self.DATABASE_NAME]
            # Test connection
            self.client.admin.command('ping')
            logging.info("Successfully connected to MongoDB")
        except Exception as e:
            logging.error("Failed to connect to MongoDB", exc_info=True)
            raise e

    def get_database(self):
        if self.database is None:  # Change this line
            self.connect_to_mongo()
        return self.database

    def close_connection(self):
        if self.client:
            self.client.close()
            logging.info("MongoDB connection closed")

# Singleton instance for database access
mongodb_config = MongoDBConfig()
