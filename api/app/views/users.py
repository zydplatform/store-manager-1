
from flask import jsonify, abort, request
from api.app import app
from api.app.models import attendants
from api.app.models.users import Attendants

@app.route('/api/v1/attendants/', methods=['POST'])
def add_store_attendant():
    data = request.json

    try:

        if ("id_number" not in data or data["id_number"] == ""):
            return jsonify({"error": "Provide Attendant ID Number"})
        elif (isinstance(data["id_number"], str)):
            id_number = data["id_number"]
            attendant_username = data["id_number"]
            attendant_password = data["id_number"]
        else:
            return jsonify({"error": "Invalid Attendant ID Number"})

        if ("attendant_name" not in data or data["attendant_name"] == ""):
            return jsonify({"error": "Provide Attendant Name"})
        elif (isinstance(data["attendant_name"], str)):
            attendant_name = data["attendant_name"]
        else:
            return jsonify({"error": "Invalid Attendant Name"})

        users = Attendants(id_number, attendant_name, attendant_username, attendant_password)

        if users.add_store_attendant() is True:
            return jsonify({"message": "New store attendant added"}), 200
        else:
            return jsonify({"message": "The store attendant is already registered"})

    except ValueError:
        return jsonify({"message": "Provide product details"})

@app.route('/api/v1/attendants/', methods=['GET'])
def view_all_store_attendants():
    return jsonify({"attendants": attendants}), 200

@app.route('/api/v1/attendants/<int:attendant_id>/', methods=['GET'])
def view_astore_attendant_details(attendant_id):
    attendant = [attendant for attendant in attendants if attendant["attendant_id"] == attendant_id]

    if len(attendant) == 0:
        return jsonify({"message": f"The attendant doesn't exist"}), 404

    return jsonify({"attendant": attendant[0]}), 200

@app.route('/api/v1/attendants/<int:attendant_id>', methods=['PUT'])
def edit_astore_attendant(attendant_id):
    data = request.json

    try:
        attendant = [attendant for attendant in attendants if attendant["attendant_id"] == attendant_id]

        if len(attendant) == 0:
            return jsonify({"message": f"The attendant doesn't exist"}), 404
        else:

            if ("id_number" not in data or data["id_number"] == ""):
                return jsonify({"error": "Provide attendant ID number"})
            elif (isinstance(data["id_number"], (int, float))):
                return jsonify({"error": "Invalid attendant ID Number"})

            if ("attendant_name" not in data or data["attendant_name"] == ""):
                return jsonify({"error": "Provide attendant name"})
            elif (isinstance(data["attendant_name"], (int, float))):
                return jsonify({"error": "Invalid attendant name"})

            if ("attendant_username" not in data or data["attendant_username"] == ""):
                return jsonify({"error": "Provide attendant username"})
            elif (isinstance(data["attendant_username"], (int, float))):
                return jsonify({"error": "Invalid attendant username"})

            if ("attendant_password" not in data or data["attendant_password"] == ""):
                return jsonify({"error": "Provide attendant password"})

            user = Attendants(data["id_number"], data["attendant_name"], data["attendant_username"], data["attendant_password"])

            if user.update_store_attendant(attendant):
                return jsonify({"message": f"{attendant[0]['attendant_name']} updated"}), 200
            else:
                return jsonify({"message": f"{attendant[0]['attendant_name']} not updated"}), 200
    except:
        abort(500)

@app.route('/api/v1/attendants/<int:attendant_id>', methods=['DELETE'])
def delete_astore_attendant(attendant_id):
    attendant = [attendant for attendant in attendants if attendant["attendant_id"] == attendant_id]

    if len(attendant) == 0:
        return jsonify({"message": f"The attendant doesn't exist"}), 404

    attendants.remove(attendant[0])
    
    return jsonify({"message": f"{attendant[0]['attendant_name']} removed"}), 200
