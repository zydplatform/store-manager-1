""" file with all user routes """

from flask import jsonify, abort, request
from api.app import app
from api.app.models.users import User

@app.route('/api/v1/auth/signup', methods=['POST'])
def add_new_user():
    """ add new user method """
    data = request.json

    try:

        if ("id_number" not in data or data["id_number"] == ""):
            return jsonify({"error": "Provide User ID Number"})
        elif (isinstance(data["id_number"], str)):
            id_number = data["id_number"]
            username = data["id_number"]
            password = data["id_number"]
        else:
            return jsonify({"error": "Invalid User ID Number"})

        if ("full_name" not in data or data["full_name"] == ""):
            return jsonify({"error": "Provide User Full Name"})
        elif (isinstance(data["full_name"], str)):
            full_name = data["full_name"]
        else:
            return jsonify({"error": "Invalid User Full Name"})

        users = User()

        if users.register_user(id_number, full_name, username, password):
            return jsonify({"message": "New User added"}), 200
        else:
            return jsonify({"message": "The User is already registered"})

    except ValueError:
        return jsonify({"message": "Provide User details"})
