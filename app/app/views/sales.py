
from flask import jsonify, abort, request
from app import app
from app.models import sales
from app.models.sales import Sales



@app.route('/api/v1/admin/sales/', methods=['GET'])
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
            else:
                abort(500)
    except:
        abort(500)

@app.route('/api/v1/admin/sales/<int:sales_id>', methods=['DELETE'])
def delete_asale(sales_id):
    sale = [sale for sale in sales if sale["sales_id"] == sales_id]

    if len(sale) == 0:
        abort(404)

    sales.remove(sale[0])
    
    return jsonify({"sale_removed": f"sale of {sale[0]['product']} canceled"}), 200
