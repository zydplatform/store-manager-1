
from flask import jsonify, abort, request
from app import app
from app.models import sales


@app.route('/api/v1/admin/sales/', methods=['GET'])
def view_all_sales():
    return jsonify({"sales": sales}), 200

