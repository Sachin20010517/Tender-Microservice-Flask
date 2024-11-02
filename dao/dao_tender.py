from config import db

class TenderDAO:
    @staticmethod
    def create_tender(data):
        return db["tenders"].insert_one(data)
    
    @staticmethod
    def get_tender(tender_id):
        return db["tenders"].find_one({"tenderId": tender_id}, {"_id": 0})
    
    @staticmethod
    def update_tender(tender_id, data):
        result = db["tenders"].update_one({"tenderId": tender_id}, {"$set": data})
        return result.matched_count > 0

    @staticmethod
    def delete_tender(tender_id):
        result = db["tenders"].delete_one({"tenderId": tender_id})
        return result.deleted_count > 0

    @staticmethod
    def get_all_tenders():
        # Fetch all tenders and convert them to a serializable format
       # Exclude `_id` field by setting it to 0
        return list(db["tenders"].find({}, {"_id": 0}))
