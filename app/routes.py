from flask import Blueprint, request, jsonify
from bson import ObjectId
from . import mongo
from .utils import handle_database_error

api = Blueprint('api', __name__)

def is_valid_objectid(value):
    try:
        ObjectId(value)
        return True
    except Exception:
        return False

def validate_data(data):
    if 'user_id' not in data or not is_valid_objectid(data['user_id']):
        return "Invalid or missing user_id", 400

    if 'stripe_customer_id' not in data or not isinstance(data['stripe_customer_id'], str):
        return "Invalid or missing stripe_customer_id", 400

    if 'user_stripe_info' not in data or not isinstance(data['user_stripe_info'], dict):
        return "Invalid or missing user_stripe_info", 400

    stripe_info = data['user_stripe_info']
    if 'subscription' not in stripe_info or not isinstance(stripe_info['subscription'], str):
        return "Invalid or missing subscription in user_stripe_info", 400
    if 'invoice_id' not in stripe_info or not isinstance(stripe_info['invoice_id'], str):
        return "Invalid or missing invoice_id in user_stripe_info", 400

    if 'user_contract' not in data or not isinstance(data['user_contract'], str) or not data['user_contract'].startswith('https://'):
        return "Invalid or missing user_contract", 400

    return None, None

@api.route('/plan', methods=['POST'])
def create_plan():
    try:
        data = request.json
        if not data:
            return jsonify({"Status": "failure", "reason": "Invalid request body"}), 400

        reason, status_code = validate_data(data)
        if reason:
            return jsonify({"Status": "failure", "reason": reason}), status_code
        
        result = mongo.db.user_payment.insert_one(data)

        if result.acknowledged:
            return jsonify({"Status": "success"}), 201
        else:
            return jsonify({"Status": "failure", "reason": "Insertion failed"}), 500

    except Exception as e:
        return handle_database_error(e)
