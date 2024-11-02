from flask import Blueprint
from api.api_create_tender_tenderId import create_tender
from api.api_get_tender_tenderId import get_tender
from api.api_update_tender_tenderId import update_tender
from api.api_delete_tender_tenderId import delete_tender
from api.api_getAll_tenders import get_all_tender

# Blueprint for grouping routes
tender_bp = Blueprint('tender_bp', __name__, url_prefix='/Tender/api')

# Route mappings for each CRUD operation
tender_bp.add_url_rule('/CreateTender', 'create_tender', create_tender, methods=['POST'])
tender_bp.add_url_rule('/UpdateTender', 'update_tender', update_tender, methods=['PUT'])
tender_bp.add_url_rule('/DeleteTender', 'delete_tender', delete_tender, methods=['DELETE'])
tender_bp.add_url_rule('/FindTender', 'get_tender', get_tender, methods=['GET'])
tender_bp.add_url_rule('/FindallTender', 'get_all_tenders', get_all_tender, methods=['GET'])


def init_app(app):
    # Register the Blueprint with the Flask app
    app.register_blueprint(tender_bp)