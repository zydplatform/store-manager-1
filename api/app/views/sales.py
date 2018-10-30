
from flask import jsonify, abort, request
from api.app import app
from api.app.models import MINIMUM_STOCK_ALLOWED
from api.app.models.sales import Sales


@app.route('/api/v1/sales/', methods=['POST'])
def make_sale():
    data = request.json

    try:
        if ("seller" not in data or data["seller"] == ""):
            return jsonify({"error": "No Seller making the sale"})
        elif (isinstance(data["seller"], str)):
            seller = data["seller"]
        else:
            return jsonify({"error": "Un Authourised access"})

        if ("product" not in data or data["product"] == ""):
            return jsonify({"error": "Add products to the sales record"})
        elif (isinstance(data["product"], str)):
            product = data["product"]
        else:
            return jsonify({"error": "Un registered stock products"})

        if ("price" not in data or data["price"] == None):
            return jsonify({"error": "Provide product price"})
        elif (isinstance(data["price"], int) and data["price"] > 0):
            price = data["price"]
        else:
            return jsonify({"error": "Invalid Product Price"})

        if ("quantity" not in data or data["quantity"] == None):
            return jsonify({"error": "Provide Product Quantity"})
        elif (isinstance(data["quantity"], (str, float))):
            return jsonify({"error": "Invalid Product Quantity"})
        elif (isinstance(data["quantity"], int) and data["quantity"] < MINIMUM_STOCK_ALLOWED):
            quantity = data["quantity"]
        else:
            return jsonify({"error": "Product Quantity leaves less than the MINIMUM STOCK ALLOWED in the inventory"})

        if ("total_cost" not in data or data["total_cost"] == None):
            return jsonify({"error": "Provide total cost of sale products"})
        elif (isinstance(data["total_cost"], (str))):
            return jsonify({"error": "Invalid total cost"})
        elif (isinstance(data["total_cost"], int)):
            total_cost = data["total_cost"]

        if ("date_sold" not in data or data["date_sold"] == ""):
            return jsonify({"error": "No dates"})
        elif (isinstance(data["date_sold"], str)):
            date_sold = data["date_sold"]
        else:
            return jsonify({"error": "Wrong dates"})

        inventory = Sales(seller, product, price, quantity, total_cost, date_sold)

        if inventory.make_sale() is True:
            return jsonify({"sale_made": "product sold"}), 200
        else:
            return jsonify({"not_sold": "product not sold"})
    except ValueError:
        return jsonify({"message": "No Sale record details"})

@app.route('/api/v1/sales/', methods=['GET'])
def view_all_sales():
    return jsonify({"sales": sales}), 200

@app.route('/api/v1/sales/<int:sales_id>/', methods=['GET'])
def view_asale_details(sales_id):
    sale = [sale for sale in sales if sale["sales_id"] == sales_id]

    if len(sale) == 0:
        return jsonify({"message": f"No such sales record found"})

    return jsonify({"sale": sale[0]}), 200

@app.route('/api/v1/sales/<int:sales_id>', methods=['PUT'])
def edit_asale(sales_id):
    data = request.json

    try:

        sale = [sale for sale in sales if sale["sales_id"] == sales_id]

        if len(sale) == 0:
            return jsonify({"message": f"No such sales record found"})
        else:
            if ("seller" not in data or data["seller"] == ""):
                return jsonify({"error": "No Seller Making this sale"})
            elif (isinstance(data["seller"], (int, float))):
                return jsonify({"error": "Un Authourised access"})

            if ("product" not in data or data["product"] == ""):
                return jsonify({"error": "Provide product name"})
            elif (isinstance(data["product"], (int, float))):
                return jsonify({"error": "Un registered stock products"})

            if ("price" not in data or data["price"] == ""):
                return jsonify({"error": "Provide product price"})
            elif (isinstance(data["price"], (str, float)) and data["price"] <= 0):
                return jsonify({"error": "Invalid Product Price"})

            if ("quantity" not in data or data["quantity"] == ""):
                return jsonify({"error": "Provide product quantity"})
            elif (isinstance(data["quantity"], (str, float))):
                return jsonify({"error": "Invalid Product Quantity"})

            if ("total_cost" not in data or data["total_cost"] == ""):
                return jsonify({"error": "No total cost for product calculated"})
            elif (isinstance(data["total_cost"], (str))):
                return jsonify({"error": "Invalid total cost"})

            if ("date_sold" not in data or data["date_sold"] == ""):
                return jsonify({"error": "No date when sale was made"})
            elif (isinstance(data["date_sold"], (int, float))):
                return jsonify({"error": "Wrong dates"})

            inventory = Sales(data["seller"], data["product"], data["price"], data["quantity"], data["total_cost"], data["date_sold"])
            if inventory.modify_sale(sale):
                return jsonify({"message": f"Sale of {sale[0]['product']} modified"}), 200
            else:
                return jsonify({"message": f"Sale of {sale[0]['product']} was not modify"})
    except:
        abort(500)

@app.route('/api/v1/sales/<int:sales_id>', methods=['DELETE'])
def delete_asale(sales_id):
    sale = [sale for sale in sales if sale["sales_id"] == sales_id]

    if len(sale) == 0:
        return jsonify({"message": f"No such sales record found"})

    sales.remove(sale[0])
    
    return jsonify({"message": f"sale of {sale[0]['product']} canceled"}), 200
