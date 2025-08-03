from pymongo import MongoClient
from utils.config import MONGO_URL, MONGO_DB_NAME

class MongoDB:
    def __init__(self):
        self.db_name = MONGO_DB_NAME
        self.db_url = MONGO_URL
        self.db = None
        self.client = None
    
    def connect(self):
        self.client = MongoClient(self.db_url)
        self.db = self.client[self.db_name]
        print(f"Connected to MongoDb {MONGO_DB_NAME}")
    
    def disconnect(self):
        if self.client:
            self.client.close()
            print("MongoDB Disconnected")
        
    def get_db(self):
        if not self.db:
            raise Exception("Database not connected. Call connect() first.")
        return self.db
    