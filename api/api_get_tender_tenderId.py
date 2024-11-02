from flask import jsonify, request
from utils.fileHandler import handle_error
from dao.dao_tender import TenderDAO

@handle_error
def get_tender():
    tender_id = request.args.get("tenderId")  # Retrieve tenderId from query parameters
    if not tender_id:
        return jsonify({"error": "tenderId query parameter is required"}), 400

    tender = TenderDAO.get_tender(tender_id)
    if tender is None:
        return jsonify({"error": "Tender not found"}), 404
    return jsonify(tender), 200
