
from flask import jsonify
from app import app
from app.models import products


@app.route('/api/v1/admin/products', methods=['GET'])
@app.route('/api/v1/attendant/products', methods=['GET'])
def view_all_products():
    return jsonify({"Products": products}), 200
