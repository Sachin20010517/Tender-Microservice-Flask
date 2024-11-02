from flask import Blueprint
from api.api_create_tender_tenderId import create_tender
from api.api_get_tender_tenderId import get_tender
from api.api_update_tender_tenderId import update_tender
from api.api_delete_tender_tenderId import delete_tender
from api.api_getAll_tenders import get_all_tender

tender_bp = Blueprint('tender_bp', __name__)

# Routes for each CRUD operation
tender_bp.route('/CreateTender', methods=['POST'])(create_tender)
tender_bp.route('/FindTender', methods=['GET'])(get_tender)
tender_bp.route('/UpdateTender', methods=['PUT'])(update_tender)
tender_bp.route('/DeleteTender', methods=['DELETE'])(delete_tender)
tender_bp.route('/FindAllTenders', methods=['GET'])(get_all_tender)

