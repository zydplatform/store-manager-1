
from flask import jsonify, abort, request
from api.app import app
from api.app.models import sales
from api.app.models.sales import Sales


@app.route('/api/v1/admin/sales/', methods=['POST'])
@app.route('/api/v1/attendant/sales/', methods=['POST'])
def make_sale():
    data = request.json

    seller = data["seller"]
    product = data["product"]
    price = data["price"]
    quantity = data["quantity"]
    total_cost = data["total_cost"]
    date_sold = data["date_sold"]

    inventory = Sales(seller, product, price, quantity, total_cost, date_sold)

    if inventory.make_sale() is True:
        return jsonify({"sale_made": "product sold"}), 200
    else:
        return jsonify({"not_sold": "product not sold"})

@app.route('/api/v1/admin/sales/', methods=['GET'])
@app.route('/api/v1/attendant/sales/', methods=['GET'])
def view_all_sales():
    return jsonify({"sales": sales}), 200

@app.route('/api/v1/admin/sales/<int:sales_id>/', methods=['GET'])
@app.route('/api/v1/attendant/sales/<int:sales_id>/', methods=['GET'])
def view_asale_details(sales_id):
    sale = [sale for sale in sales if sale["sales_id"] == sales_id]

    if len(sale) == 0:
        abort(404)

    return jsonify({"sale": sale[0]}), 200

@app.route('/api/v1/admin/sales/<int:sales_id>', methods=['PUT'])
def edit_asale(sales_id):
    data = request.json

    try:
        sale = [sale for sale in sales if sale["sales_id"] == sales_id]

        if len(sale) == 0:
            abort(500)
        else:
            inventory = Sales(data["seller"], data["product"], data["price"], data["quantity"], data["total_cost"], data["date_sold"])
            if inventory.modify_sale(sale):
                return jsonify({"sale_modified": f"sale of {sale[0]['product']} modified"}), 200
            # else:
            #     abort(500)
    except:
        abort(500)

@app.route('/api/v1/admin/sales/<int:sales_id>', methods=['DELETE'])
def delete_asale(sales_id):
    sale = [sale for sale in sales if sale["sales_id"] == sales_id]

    if len(sale) == 0:
        abort(404)

    sales.remove(sale[0])
    
    return jsonify({"sale_removed": f"sale of {sale[0]['product']} canceled"}), 200
