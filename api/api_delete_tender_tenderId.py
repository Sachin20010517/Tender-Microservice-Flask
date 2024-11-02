from flask import jsonify, request
from utils.fileHandler import handle_error
from dao.dao_tender import TenderDAO

@handle_error
def delete_tender():

    tender_id = request.args.get("tenderId")  # Retrieve tenderId from query parameters
    if not tender_id:
        return jsonify({"error": "tenderId query parameter is required"}), 400

    deleted = TenderDAO.delete_tender(tender_id)
    if not deleted:
        return jsonify({"error": "Tender not found"}), 404
    return jsonify({"message": "Tender deleted successfully"}), 200
