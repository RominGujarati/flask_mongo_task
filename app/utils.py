from flask import jsonify

def handle_database_error(exception):
    print(f"Database error: {exception}")
    return jsonify({"Status": "failure", "reason": "Database is not available"}), 500
