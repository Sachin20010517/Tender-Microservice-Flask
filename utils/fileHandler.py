# utils/error_handler.py
import logging
from functools import wraps
from flask import jsonify

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_error(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError as e:
            # Handle ValueError specifically
            logging.error(f"ValueError: {str(e)}")  # Log the error for debugging
            return jsonify({"error": str(e)}), 400  # Use 400 for client errors
        except KeyError as e:
            # Handle KeyError for missing keys
            logging.error(f"KeyError: {str(e)}")  # Log the error
            return jsonify({"error": f"Missing key: {str(e)}"}), 400  # Return 400 for client errors
        except Exception as e:
            # Log unexpected errors
            logging.error(f"Unexpected error: {str(e)}")  # Log the error
            return jsonify({"error": "An unexpected error occurred"}), 500  # Return 500 for server errors
    return decorated_function
