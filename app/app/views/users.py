
from flask import jsonify, abort, request
from app import app
from app.models import attendants
from app.models.users import Attendants

@app.route('/api/v1/admin/attendants/', methods=['POST'])
def add_store_attendant():
    data = request.json

    id_number = data["id_number"]
    attendant_name = data["attendant_name"]
    attendant_username = data["attendant_username"]
    attendant_password = data["attendant_password"]

    users = Attendants(id_number, attendant_name, attendant_username, attendant_password)

    if users.add_store_attendant() is True:
        return jsonify({"attendant_added": "New store attendant added"}), 200
    else:
        return jsonify({"attendant_available": "The store attendant is already added"})


@app.route('/api/v1/admin/attendants/', methods=['GET'])
def view_all_store_attendants():
    return jsonify({"attendants": attendants}), 200

@app.route('/api/v1/admin/attendants/<int:attendant_id>/', methods=['GET'])
def view_astore_attendant_details(attendant_id):
    attendant = [attendant for attendant in attendants if attendant["attendant_id"] == attendant_id]

    if len(attendant) == 0:
        abort(404)

    return jsonify({"attendant": attendant[0]}), 200


@app.route('/api/v1/admin/attendants/<int:attendant_id>', methods=['DELETE'])
def delete_astore_attendant(attendant_id):
    attendant = [attendant for attendant in attendants if attendant["attendant_id"] == attendant_id]

    if len(attendant) == 0:
        abort(404)

    attendants.remove(attendant[0])
    
    return jsonify({"attendant_removed": f"{attendant[0]['attendant_name']} removed"}), 200
