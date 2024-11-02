# api_handler/tender_routes.py

from flask import Blueprint, request, jsonify
from api.api_create_tender import TenderAPI
from utils.fileHandler import handle_error

tender_bp = Blueprint('tender_bp', __name__)

@tender_bp.route('/tender', methods=['POST'])
@handle_error
def create_tender():
    data = request.json
    tender_id = TenderAPI.create_tender(data)
    return jsonify({"message": "Tender created", "tenderId": tender_id}), 201

@tender_bp.route('/tender/<tender_id>', methods=['GET'])
@handle_error
def get_tender(tender_id):
    tender = TenderAPI.get_tender(tender_id)
    return jsonify(tender), 200

@tender_bp.route('/tenders', methods=['GET'])
@handle_error
def get_all_tenders():
    tenders = TenderAPI.get_all_tenders()
    return jsonify(tenders), 200

@tender_bp.route('/tender/<tender_id>', methods=['PUT'])
@handle_error
def update_tender(tender_id):
    data = request.json
    message = TenderAPI.update_tender(tender_id, data)
    return jsonify({"message": message}), 200

@tender_bp.route('/tender/<tender_id>', methods=['DELETE'])
@handle_error
def delete_tender(tender_id):
    message = TenderAPI.delete_tender(tender_id)
    return jsonify({"message": message}), 200
