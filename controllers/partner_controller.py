from flask import Blueprint, request, jsonify
from services.partner_service import list_partners, add_new_partner, add_new_account

partner_blueprint = Blueprint('partner_blueprint', __name__)

@partner_blueprint.route('/partners', methods=['GET'])
def get_partners():
    partners = list_parteners()
    return jsonify([partner.to_dict() for partner in partners])

@partner_blueprint.route('/partners', methods=['POST'])
def post_partner():
    data = request.get_json()
    partner = add_new_partner(data['name'], data['email'], data['phone'])
    return jsonify(partner.to_dict()), 201

@partner_blueprint.route('/accounts', methods=['POST'])
def post_account():
    data = request.get_json()
    account = add_new_account(data['partner_id'], data['account_type'], data['balance'])
    return jsonify(account.to_dict()), 201
