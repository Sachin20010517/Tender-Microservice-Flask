# dao/tender_dao.py

from bson.objectid import ObjectId
from dto.model_tender import TenderDTO
from config import db  # Import `db` instance from config

tender_collection = db["tenders"]

class TenderDAO:
    @staticmethod
    def create_tender(tender_data: dict) -> str:
        result = tender_collection.insert_one(tender_data)
        return str(result.inserted_id)

    @staticmethod
    def get_tender(tender_id: str) -> dict:
        return tender_collection.find_one({"_id": ObjectId(tender_id)})

    @staticmethod
    def get_all_tenders() -> list:
        return list(tender_collection.find())

    @staticmethod
    def update_tender(tender_id: str, tender_data: dict) -> int:
        result = tender_collection.update_one(
            {"_id": ObjectId(tender_id)},
            {"$set": tender_data}
        )
        return result.modified_count

    @staticmethod
    def delete_tender(tender_id: str) -> int:
        result = tender_collection.delete_one({"_id": ObjectId(tender_id)})
        return result.deleted_count
