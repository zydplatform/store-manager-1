
from flask import jsonify, abort, request
from app import app
from app.models import products, MINIMUM_STOCK_ALLOWED
from app.models.products import Products


@app.route('/api/v1/admin/products/', methods=['POST'])
def add_product():
    data = request.json

    product_name = data["product_name"]
    product_category = data["product_category"]
    product_price = data["product_price"]
    product_quantity = data["product_quantity"]
    product_minimum_stock_allowed = MINIMUM_STOCK_ALLOWED

    inventory = Products(product_name, product_category, product_price, product_quantity, product_minimum_stock_allowed)

    if inventory.add_product() is True:
        return jsonify({"product_added": "The product has been added in the inventory"}), 200
    else:
        return jsonify({"product_available": "The product is already added in the inventory"})

@app.route('/api/v1/admin/products/', methods=['GET'])
@app.route('/api/v1/attendant/products/', methods=['GET'])
def view_all_products():
    return jsonify({"Products": products}), 200

@app.route('/api/v1/admin/products/<int:product_id>/', methods=['GET'])
@app.route('/api/v1/admin/attendant/<int:product_id>/', methods=['GET'])
def view_aproduct_details(product_id):
    product = [product for product in products if product["product_id"] == product_id]

    if len(product) == 0:
        abort(404)

    return jsonify({"Product": product[0]}), 200

@app.route('/api/v1/admin/products/<int:product_id>', methods=['PUT'])
def edit_aproduct(product_id):
    data = request.json

    try:
        product = [product for product in products if product["product_id"] == product_id]

        if len(product) == 0:
            abort(500)
        else:
            inventory = Products(data["product_name"], data["product_category"], data["product_price"], data["product_quantity"], data["product_minimum_stock_allowed"])
            if inventory.update_product(product):
                return jsonify({"Updated": f"{product[0]['product_name']} updated"}), 200
            else:
                abort(500)
    except:
        abort(500)

@app.route('/api/v1/admin/products/<int:product_id>', methods=['DELETE'])
def delete_aproduct(product_id):
    product = [product for product in products if product["product_id"] == product_id]

    if len(product) == 0:
        abort(404)

    products.remove(product[0])
    
    return jsonify({"product_removed": f"{product[0]['product_name']} removed from inventory"}), 200
