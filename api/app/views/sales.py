""" file with all sales and sales routes """

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, abort, request
from api.app import app
from api.app.models.sales import Sale

@app.route('/api/v1/sales', methods=['POST'])
@jwt_required
def make_sale():
    """ make anew sale """

    logged_in_user = get_jwt_identity()

    if not logged_in_user["role"]:
        return jsonify({"error": "Unauthorized Access"}), 401

    data = request.json 

    try:

        if ("product" not in data or data["product"] == ""):
            return jsonify({"error": "Add products to the sales record"})
        elif (isinstance(data["product"], (str, float))):
            return jsonify({"error": "Invalid Product Id"})
        elif (isinstance(data["product"], int)):
            product = data["product"]

        if ("quantity" not in data or data["quantity"] == None):
            return jsonify({"error": "Provide Product Quantity"})
        elif (isinstance(data["quantity"], (str, float))):
            return jsonify({"error": "Invalid Product Quantity"})
        elif (isinstance(data["quantity"], int)):
            quantity = data["quantity"]
        else:
            return jsonify({"error": "Product Quantity leaves less than the MINIMUM STOCK ALLOWED in the inventory"})

        inventory = Sale(product, quantity, logged_in_user["id"])

        sale_details = inventory.make_sale()

        if sale_details:
            return jsonify({"message": "product sold", "sale_details" : sale_details}), 200
        else:
            return jsonify({"error": "product doesn't exist"})
    except ValueError:
        return jsonify({"error": "No Sale record details"})

@app.route('/api/v1/sales', methods=['GET'])
@jwt_required
def view_all_sales():

    logged_in_user = get_jwt_identity()
    
    sales = Sale(products = "", quantity = 0, seller = logged_in_user["id"])
    all_sales_records  =sales.get_all_sales()

    if not all_sales_records:
        return jsonify({"error": "No Sales Made Yet"}), 404
    
    return jsonify({"sales_records": all_sales_records}), 200

@app.route('/api/v1/sales/<int:sales_id>', methods=['GET'])
@jwt_required
def view_asale_details(sales_id):

    logged_in_user = get_jwt_identity()
    
    sales = Sale(products = "", quantity = 0, seller = logged_in_user["id"])

    sale_record_details = sales.get_aspecific_sales_record(sales_id)

    if not sale_record_details:
        return jsonify({"error": f"No such sales record found"}), 404

    return jsonify({"sales_details": sale_record_details}), 200


