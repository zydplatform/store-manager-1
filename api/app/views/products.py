""" file with all products and product_categories routes """

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, abort, request
from api.app import app
from api.app.models import MINIMUM_STOCK_ALLOWED
from api.app.models.products import Product, ProductCategory


@app.route('/api/v1/products', methods=['POST'])
@jwt_required
def add_product():
    """ add new product to inventory """

    logged_in_user = get_jwt_identity()

    if logged_in_user["role"] == "attendant":
        return jsonify({"error": "Unauthorized Access"}), 401

    data = request.json 

    try:

        if ("product_name" not in data or data["product_name"] == ""):
            return jsonify({"error": "Provide Product name"}), 400
        elif (isinstance(data["product_name"], str)):
            product_name = data["product_name"]
        else:
            return jsonify({"error": "Invalid Product name"}), 400

        if ("product_category" not in data or data["product_category"] == ""):
            return jsonify({"error": "Provide product category"}), 400
        elif (isinstance(data["product_category"], int)):
            product_category = data["product_category"]
        else:
            return jsonify({"error": "Invalid Product Category name"}), 400

        if ("product_price" not in data or data["product_price"] == None):
            return jsonify({"error": "Provide product price"}), 400
        elif (isinstance(data["product_price"], int) and data["product_price"] > 0):
            product_price = data["product_price"]
        else:
            return jsonify({"error": "Invalid Product Price"}), 400

        if ("product_quantity" not in data or data["product_quantity"] == None):
            return jsonify({"error": "Provide Product Quantity"}), 400
        elif (isinstance(data["product_quantity"], (str, float))):
            return jsonify({"error": "Invalid Product Quantity"}), 400
        elif (isinstance(data["product_quantity"], int) and data["product_quantity"] > MINIMUM_STOCK_ALLOWED):
            product_quantity = data["product_quantity"]
        else:
            return jsonify({"error": "Product Quantity is less than the MINIMUM STOCK ALLOWED"}), 400

        if ("product_minimum_stock_allowed" not in data or data["product_minimum_stock_allowed"] == None):
            product_minimum_stock_allowed = MINIMUM_STOCK_ALLOWED
        elif (isinstance(data["product_minimum_stock_allowed"], (str, float)) or int(data["product_minimum_stock_allowed"]) == 0):
            return jsonify({"error": "Invalid minimum stock value"}), 400
        elif (int(data["product_minimum_stock_allowed"]) > 0):
            product_minimum_stock_allowed = data["product_minimum_stock_allowed"]   

        inventory = Product()

        added_product_details = inventory.add_product(product_name, product_category, product_price, 
            product_quantity, product_minimum_stock_allowed, logged_in_user["id"])

        product_details = {
            "product_id" : added_product_details[0],
            "product_name" : added_product_details[1],
            "product_category" : added_product_details[2],
            "product_price" : added_product_details[3], 
            "product_quantity" : added_product_details[4],
            "product_minimum_stock_allowed" : added_product_details[4]
        }

        if added_product_details:
            return jsonify({"message": "Product added", "product_details": product_details}), 200
        else:
            return jsonify({"error": "Product exists"})

    except ValueError:
        return jsonify({"error": "Provide product details"}), 400

@app.route('/api/v1/products/', methods=['GET'])
@jwt_required
def view_all_products():
    
    inventory = Product()
    products = inventory.get_all_products()

    if len(products) == 0:
        return jsonify({"message": "No products added Yet"}), 404
    
    return jsonify({"Products": products}), 200

@app.route('/api/v1/products/<int:product_id>/', methods=['GET'])
@jwt_required
def view_aproduct_details(product_id):

    inventory = Product()
    product = inventory.get_a_product_by_id(product_id)

    if len(product) == 0:
        return jsonify({"error": f"The product doesn't exist"}), 404

    return jsonify({"Product": product}), 200

@app.route('/api/v1/products/<int:product_id>', methods=['PUT'])
@jwt_required
def edit_aproduct(product_id):
    data = request.json

    try:
        logged_in_user = get_jwt_identity()

        if logged_in_user["role"] == "attendant":
            return jsonify({"error": "Unauthorized Access"}), 401

        inventory = Product()

        product_details = inventory.get_a_product_by_id(product_id)

        product = [product for product in product_details if product_details["product_id"] == product_id]

        if len(product) == 0:
            return jsonify({"error": f"The product is not available"}), 404
        else:
            if ("product_name" not in data or data["product_name"] == ""):
                return jsonify({"error": "Provide product name"}), 400        
            
            if ("product_category" not in data or data["product_category"] == ""):
                return jsonify({"error": "Provide product category name"}), 400
            
            if ("product_price" not in data or data["product_price"] == ""):
                return jsonify({"error": "Provide product price"}), 400
            
            if ("product_quantity" not in data or data["product_quantity"] == ""):
                return jsonify({"error": "Provide product Quantity"}), 400
            
            if ("product_minimum_stock_allowed" not in data or data["product_minimum_stock_allowed"] == None):
                return jsonify({"error": "Provide the MINIMUM STOCK ALLOWED"}), 400

            updated_product = inventory.update_product(product_id, data["product_name"], data["product_category"], data["product_price"], data["product_quantity"], data["product_minimum_stock_allowed"], logged_in_user["id"])
            
            if updated_product:
                return jsonify({"message": f"{updated_product} updated"}), 200
            else:
                return jsonify({"error": f"{updated_product} not updated"}), 500
    except:
        abort(500)

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_aproduct(product_id):

    inventory = Product()

    product_details = inventory.get_a_product_by_id(product_id)

    product = [product for product in product_details if product_details["product_id"] == product_id]

    if len(product) == 0:
        return jsonify({"error": f"The product doesn't exist"}), 400
    else:
        deleted_product = inventory.remove_a_specific_product(product_id)   
        return jsonify({"message": f"{deleted_product} removed"}), 200



@app.route('/api/v1/products_categories', methods=['POST'])
@jwt_required
def add_product_category():

    logged_in_user = get_jwt_identity()

    if logged_in_user["role"] == "attendant":
        return jsonify({"error": "Unauthorized Access"}), 401

    data = request.json
    try:
        if ("category_name" not in data or data["category_name"] == ""):
            return jsonify({"error": "Provide product category name"}), 400
        elif (isinstance(data["category_name"], str)):
            category_name = data["category_name"]
        elif (isinstance(data["category_name"], int)):
            return jsonify({"error": "Invalid product category name"}), 400

        category_name = data["category_name"]

        inventory = ProductCategory()

        product_category_details = {
            "category_name" : category_name
        }

        if inventory.add_product_category(category_name, logged_in_user["id"]):
            return jsonify({"message": "Product category added", "category_details" : product_category_details}), 200
        else:
            return jsonify({"error": "Product category exists"})
    except ValueError:
        return jsonify({"error": "Provide product category details"}), 400

@app.route('/api/v1/products_categories', methods=['GET'])
@jwt_required
def view_all_product_categories():
    
    inventory = ProductCategory()
    product_categories = inventory.get_all_product_categories()

    if len(product_categories) == 0:
        return jsonify({"error": "No product categories added yet"}), 404

    return jsonify({"Product_categories" : product_categories}), 200

@app.route('/api/v1/products_categories/<int:category_id>/', methods=['GET'])
@jwt_required
def view_aproduct_category_details(category_id):

    inventory = ProductCategory()
    product_category = inventory.get_a_product_category_by_id(category_id)

    if len(product_category) == 0:
        return jsonify({"error": "Product category does not exist"}), 400

    return jsonify({"Product_category" : product_category}), 200

@app.route('/api/v1/products_categories/<int:category_id>', methods=['PUT'])
@jwt_required
def edit_aproduct_category(category_id):
    data = request.json

    try:

        logged_in_user = get_jwt_identity()

        if logged_in_user["role"] == "attendant":
            return jsonify({"error": "Unauthorized Access"}), 401

        if ("category_name" not in data or data["category_name"] == ""):
            return jsonify({"error": "Provide product category name"}), 400
        elif (isinstance(data["category_name"], str)):
            category_name = data["category_name"]
        elif (isinstance(data["category_name"], int)):
            return jsonify({"error": "Invalid product category name"}), 400

        inventory = ProductCategory()

        product_category_details = inventory.get_a_product_category_by_id(category_id)

        if len(product_category_details) == 0:
            return jsonify({"error": "The product category does not exist"}), 404
        else:
            if inventory.update_product_category(category_id, category_name, logged_in_user["id"]):
                return jsonify({"message": f"{product_category_details['category_name']} updated"}), 200
            else:
                return jsonify({"error": f"Product category {product_category_details['category_name']} was not updated"}), 404
    except:
        abort(500)

@app.route('/api/v1/products_categories/<int:category_id>', methods=['DELETE'])
@jwt_required
def delete_aproduct_category(category_id):

    inventory = ProductCategory()

    product_category_details = inventory.get_a_product_category_by_id(category_id)

    if len(product_category_details) == 0:
        return jsonify({"error": f"The product category doesn't exist"}), 404
    else:
        deleted_category = inventory.remove_a_specific_product_category(category_id)   
        return jsonify({"message": f"{deleted_category} removed"}), 200

