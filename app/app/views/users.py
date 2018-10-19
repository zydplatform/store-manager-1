
from flask import jsonify, abort, request
from app import app
from app.models import attendants


@app.route('/api/v1/admin/attendants/', methods=['GET'])
def view_all_store_attendants():
    return jsonify({"attendants": attendants}), 200

@app.route('/api/v1/admin/attendants/<int:attendant_id>/', methods=['GET'])
def view_astore_attendant_details(attendant_id):
    attendant = [attendant for attendant in attendants if attendant["attendant_id"] == attendant_id]

    if len(attendant) == 0:
        abort(404)

    return jsonify({"attendant": attendant[0]}), 200
