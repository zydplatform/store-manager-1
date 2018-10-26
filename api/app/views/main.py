
from flask import jsonify
from api.app import app

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Requested Page Not found'}), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Requested Page Is Invalid'}), 400


@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server Error, Try Again'}), 500

@app.route('/')
def index():
    return "<h3>Welcome To The Store Manager System API Version 1</h3>"

@app.route('/api/v1/')
def home():
    return jsonify({"message": "Welcome To The Store Manager System API Version 1"}), 200