
from flask import jsonify, abort, request
from app import app
from app.models import attendants


@app.route('/api/v1/admin/attendants/', methods=['GET'])
def view_all_store_attendants():
    return jsonify({"attendants": attendants}), 200

