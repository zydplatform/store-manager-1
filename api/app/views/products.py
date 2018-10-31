""" file with all products and product_categories routes """

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, abort, request
from api.app import app
from api.app.models import MINIMUM_STOCK_ALLOWED
from api.app.models.products import Product


@app.route('/api/v1/products', methods=['POST'])
@jwt_required
def add_product():
    """ add new product to inventory """

    logged_in_user = get_jwt_identity()

    if logged_in_user["role"] == "attendant":
        return jsonify({"message": "Unauthorized Access"})

    data = request.json 

    try:

        if ("product_name" not in data or data["product_name"] == ""):
            return jsonify({"error": "Provide Product name"})
        elif (isinstance(data["product_name"], str)):
            product_name = data["product_name"]
        else:
            return jsonify({"error": "Invalid Product name"})

        if ("product_category" not in data or data["product_category"] == ""):
            return jsonify({"error": "Provide product category"})
        elif (isinstance(data["product_category"], int)):
            product_category = data["product_category"]
        else:
            return jsonify({"error": "Invalid Product Category name"})

        if ("product_price" not in data or data["product_price"] == None):
            return jsonify({"error": "Provide product price"})
        elif (isinstance(data["product_price"], int) and data["product_price"] > 0):
            product_price = data["product_price"]
        else:
            return jsonify({"error": "Invalid Product Price"})

        if ("product_quantity" not in data or data["product_quantity"] == None):
            return jsonify({"error": "Provide Product Quantity"})
        elif (isinstance(data["product_quantity"], (str, float))):
            return jsonify({"error": "Invalid Product Quantity"})
        elif (isinstance(data["product_quantity"], int) and data["product_quantity"] > MINIMUM_STOCK_ALLOWED):
            product_quantity = data["product_quantity"]
        else:
            return jsonify({"error": "Product Quantity is less than the MINIMUM STOCK ALLOWED"})

        if ("product_minimum_stock_allowed" not in data or data["product_minimum_stock_allowed"] == None):
            product_minimum_stock_allowed = MINIMUM_STOCK_ALLOWED
        elif (isinstance(data["product_minimum_stock_allowed"], (str, float)) or int(data["product_minimum_stock_allowed"]) == 0):
            return jsonify({"error": "Invalid minimum stock value"}) 
        elif (int(data["product_minimum_stock_allowed"]) > 0):
            product_minimum_stock_allowed = data["product_minimum_stock_allowed"]   

        inventory = Product()

        if inventory.add_product(product_name, product_category, product_price, product_quantity, product_minimum_stock_allowed, logged_in_user["id"]):
            return jsonify({"message": "The product has been added in the inventory"}), 200
        else:
            return jsonify({"message": "The product is already added in the inventory"})

    except ValueError:
        return jsonify({"message": "Provide product details"})

