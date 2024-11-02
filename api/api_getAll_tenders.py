from flask import jsonify
from utils.fileHandler import handle_error
from dao.dao_tender import TenderDAO

@handle_error
def get_all_tender():
    try:
        tenders = TenderDAO.get_all_tenders()  # Call the method to retrieve all tenders
        return jsonify(tenders), 200
    except Exception as e:
        # Log the error or return a more specific error message
        return jsonify({"error": str(e)}), 500

