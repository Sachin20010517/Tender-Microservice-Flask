from flask import request, jsonify
from utils.fileHandler import handle_error
from dao.dao_tender import TenderDAO
from validators import validate_tender_data

@handle_error
def update_tender():

    tender_id = request.args.get("tenderId")  # Retrieve tenderId from query parameters
    if not tender_id:
        return jsonify({"error": "tenderId query parameter is required"}), 400

    data = request.json
    
    # Validation
    # errors = validate_tender_data(data)
    # if errors:
    #     return jsonify({"error": errors}), 400

    updated = TenderDAO.update_tender(tender_id, data)
    if not updated:
        return jsonify({"error": "Tender not found"}), 404
    return jsonify({"message": "Tender updated successfully"}), 200
