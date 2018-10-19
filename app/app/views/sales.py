
from flask import jsonify, abort, request
from app import app
from app.models import sales


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
