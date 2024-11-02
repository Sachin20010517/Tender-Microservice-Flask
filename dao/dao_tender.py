#from config import db
from dbConfig.dbConnector import mongodb_config


class TenderDAO:
    @staticmethod
    def create_tender(data):
        db = mongodb_config.get_database()
        return db["tenders"].insert_one(data)
    
    @staticmethod
    def get_tender(tender_id):
        db = mongodb_config.get_database()
        return db["tenders"].find_one({"tenderId": tender_id}, {"_id": 0})
    
    @staticmethod
    def update_tender(tender_id, data):
        db = mongodb_config.get_database()
        result = db["tenders"].update_one({"tenderId": tender_id}, {"$set": data})
        return result.matched_count > 0

    @staticmethod
    def delete_tender(tender_id):
        db = mongodb_config.get_database()
        result = db["tenders"].delete_one({"tenderId": tender_id})
        return result.deleted_count > 0

    @staticmethod
    def get_all_tenders():
        db = mongodb_config.get_database()
        # Fetch all tenders and convert them to a serializable format
       # Exclude `_id` field by setting it to 0
        return list(db["tenders"].find({}, {"_id": 0}))
