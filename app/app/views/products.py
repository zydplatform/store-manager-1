
from flask import jsonify, abort
from app import app
from app.models import products


@app.route('/api/v1/admin/products', methods=['GET'])
@app.route('/api/v1/attendant/products', methods=['GET'])
def view_all_products():
    return jsonify({"Products": products}), 200


@app.route('/api/v1/admin/products/<int:product_id>', methods=['GET'])
@app.route('/api/v1/admin/attendant/<int:product_id>', methods=['GET'])
def view_aproduct_details(product_id):
    product = [product for product in products if product["product_id"] == product_id]

    if len(product) == 0:
        abort(404)

    return jsonify({"Product": product[0]}), 200