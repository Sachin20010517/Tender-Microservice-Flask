from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
from werkzeug.middleware.proxy_fix import ProxyFix
from apiHandler import router
#from apiHandler.router import init_app 
from utils import fileHandler
#from utils.fileHandler import handle_error
from dbConfig.dbConnector import mongodb_config

# Initialize the Flask app
app = Flask(__name__)

# Configure CORS
CORS(app, resources={r"/Tender/api/*": {"origins": "*"}})

# Set up logging
logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

# Add middleware for error recovery and other functionalities
app.wsgi_app = ProxyFix(app.wsgi_app)

# Custom middleware for logging requests and responses
@app.before_request
def log_request_info():
    app.logger.info(f"Request: {request.method} {request.path}")
    if request.data:
        app.logger.info(f"Request Data: {request.get_data()}")

@app.after_request
def log_response_info(response):
    app.logger.info(f"Response Status: {response.status}")
    return response

# Initialize database connection
try:
    db = mongodb_config.get_database()  # Get the database instance
except Exception as e:
    app.logger.error("Could not connect to the database", exc_info=True)
    exit(1)  # Exit if database connection fails

# Register routes
router.init_app(app)

# Root route
@app.route('/')
def root():
    return jsonify({"message": "Tender-APP1256 service is up and running", "version": "1.0"})

# Error handler example (could be part of `utils/error_handler.py`)
#@app.errorhandler(404)
fileHandler.handle_error(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify(error="An unexpected error occurred"), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)







# from flask import Flask, render_template
# from apiHandler.router import tender_bp

# app = Flask(__name__)

# # Register the blueprint
# app.register_blueprint(tender_bp, url_prefix='/api')


# # Define a route for the root URL
# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)


