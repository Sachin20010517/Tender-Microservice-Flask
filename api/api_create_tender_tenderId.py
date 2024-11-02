from flask import request, jsonify
from utils.fileHandler import handle_error
from dao.dao_tender import TenderDAO
import uuid
from validators import validate_tender_data

@handle_error
def create_tender():
    data = request.json
    tender_id = str(uuid.uuid4())
    data["tenderId"] = tender_id
    
    # Validation
    errors = validate_tender_data(data)
    if errors:
        return jsonify({"error": errors}), 400

    TenderDAO.create_tender(data)
    return jsonify({"message": "Tender created", "tenderId": tender_id}), 201
