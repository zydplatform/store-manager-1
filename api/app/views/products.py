
from flask import jsonify, abort, request
from api.app import app
from api.app.models import products, product_categories, MINIMUM_STOCK_ALLOWED
from api.app.models.products import Products
from api.app.models.products import ProductCategories


@app.route('/api/v1/products_categories/', methods=['POST'])
def add_product_category():
    data = request.json
    try:
        if ("category_name" not in data or data["category_name"] == ""):
            return jsonify({"error": "Provide product category name"})
        elif (isinstance(data["category_name"], str)):
            category_name = data["category_name"]
        elif (isinstance(data["category_name"], int)):
            return jsonify({"error": "Invalid product category name"})

        category_name = data["category_name"]

        inventory = ProductCategories(category_name)

        if inventory.add_product_category() is True:
            return jsonify({"message": "The product category has been added"}), 200
        else:
            return jsonify({"message": "The product category is already added"})
    except ValueError:
        return jsonify({"message": "Provide product category details"})

@app.route('/api/v1/products_categories/', methods=['GET'])
def view_all_product_categories():
    return jsonify({"product_categories": product_categories}), 200

@app.route('/api/v1/products_categories/<int:category_id>/', methods=['GET'])
def view_aproduct_category_details(category_id):
    category = [category for category in product_categories if category["category_id"] == category_id]

    if len(category) == 0:
        return jsonify({"message": f"The product category is not available"})

    return jsonify({"product_category": category[0]}), 200

@app.route('/api/v1/products_categories/<int:category_id>', methods=['PUT'])
def edit_aproduct_category(category_id):
    data = request.json

    try:

        if ("category_name" not in data or data["category_name"] == ""):
            return jsonify({"error": "Provide product category name"})
        elif (isinstance(data["category_name"], str)):
            category_name = data["category_name"]
        elif (isinstance(data["category_name"], int)):
            return jsonify({"error": "Invalid product category name"})

        category = [category for category in product_categories if category["category_id"] == category_id]

        if len(category) == 0:
            return jsonify({"message": f"The product category does not exist"})
        else:
            inventory = ProductCategories(category_name)
            if inventory.update_product_category(category):
                return jsonify({"Updated": f"{category[0]['category_name']} updated"}), 200
            else:
                return jsonify({"message": f"Product category {category[0]['category_name']} was not updated"})
    except:
        abort(500)

@app.route('/api/v1/products_categories/<int:category_id>', methods=['DELETE'])
def delete_aproduct_category(category_id):
    category = [category for category in product_categories if category["category_id"] == category_id]

    if len(category) == 0:
        return jsonify({"message": f"The product category is not available"})

    product_categories.remove(category[0])
    
    return jsonify({"product_removed": f"{category[0]['category_name']} category removed"}), 200

@app.route('/api/v1/products/', methods=['POST'])
def add_product():
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
        elif (isinstance(data["product_category"], str)):
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

        inventory = Products(product_name, product_category, product_price, product_quantity, product_minimum_stock_allowed)

        if inventory.add_product() is True:
            return jsonify({"message": "The product has been added in the inventory"}), 200
        else:
            return jsonify({"message": "The product is already added in the inventory"})

    except ValueError:
        return jsonify({"message": "Provide product details"})

@app.route('/api/v1/products/', methods=['GET'])
def view_all_products():
    return jsonify({"Products": products}), 200

@app.route('/api/v1/products/<int:product_id>/', methods=['GET'])
def view_aproduct_details(product_id):
    product = [product for product in products if product["product_id"] == product_id]

    if len(product) == 0:
        return jsonify({"message": f"The product is not available"})

    return jsonify({"Product": product[0]}), 200

@app.route('/api/v1/products/<int:product_id>', methods=['PUT'])
def edit_aproduct(product_id):
    data = request.json

    try:
        product = [product for product in products if product["product_id"] == product_id]

        if len(product) == 0:
            return jsonify({"message": f"The product is not available"})
        else:
            if ("product_name" not in data or data["product_name"] == ""):
                return jsonify({"error": "Provide product name"})        
            
            if ("product_category" not in data or data["product_category"] == ""):
                return jsonify({"error": "Provide product category name"})
            
            if ("product_price" not in data or data["product_price"] == ""):
                return jsonify({"error": "Provide product price"})
            
            if ("product_quantity" not in data or data["product_quantity"] == ""):
                return jsonify({"error": "Provide product Quantity"})
            
            if ("product_minimum_stock_allowed" not in data or data["product_minimum_stock_allowed"] == None):
                return jsonify({"error": "Provide the MINIMUM STOCK ALLOWED"})

            inventory = Products(data["product_name"], data["product_category"], data["product_price"], data["product_quantity"], data["product_minimum_stock_allowed"])
            if inventory.update_product(product):
                return jsonify({"Updated": f"{product[0]['product_name']} updated"}), 200
            else:
                abort(500)
    except:
        abort(500)

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_aproduct(product_id):
    product = [product for product in products if product["product_id"] == product_id]

    if len(product) == 0:
        return jsonify({"message": f"The product is not available"})

    products.remove(product[0])
    
    return jsonify({"product_removed": f"{product[0]['product_name']} removed from inventory"}), 200
