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

@app.route('/api/v1/users/', methods=['GET'])
def view_all_users():
    """ get all registered users"""

    user_class = User()
    users = user_class.get_all_registered_users()

    if len(users) == 0:
        return jsonify({"message": "No users registered yet"}), 404

    return jsonify({"users": users}), 200

@app.route('/api/v1/users/<int:user_id>/', methods=['GET'])
def view_a_registered_user_details(user_id):
    """" get a specific registered user """
    user_class = User()
    user = user_class.get_a_registered_user_by_id(user_id)

    if len(user) == 0:
        return jsonify({"message": f"The User doesn't exist"}), 404

    return jsonify({"user": user}), 200

@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def edit_a_speific_user_details(user_id):
    data = request.json

    try:
        user_class = User()
        user = user_class.get_a_registered_user_by_id(user_id)

        if len(user) == 0:
            return jsonify({"message": f"The User doesn't exist"}), 404
        else:
            if ("id_number" not in data or data["id_number"] == ""):
                return jsonify({"error": "Provide User ID number"})
            elif (isinstance(data["id_number"], (int, float))):
                return jsonify({"error": "Invalid User ID Number"})

            if ("full_name" not in data or data["full_name"] == ""):
                return jsonify({"error": "Provide User Full name"})
            elif (isinstance(data["full_name"], (int, float))):
                return jsonify({"error": "Invalid User Full Name"})

            if ("username" not in data or data["username"] == ""):
                return jsonify({"error": "Provide User username"})
            elif (isinstance(data["username"], (int, float))):
                return jsonify({"error": "Invalid User username"})

            if ("password" not in data or data["password"] == ""):
                return jsonify({"error": "Provide User password"})

            user_class = User()
            user = user_class.get_a_registered_user_by_id(user_id)

            if len(user) == 0:
                return jsonify({"message": f"The User doesn't exist"}), 404
            else:
                updated_user = user_class.update_a_user_details(
                    user_id, data["id_number"], data["full_name"], data["username"], data["password"], "FALSE", 1
                )

                if updated_user:
                    return jsonify({"message": f"User {updated_user} updated"}), 200
                else:
                    return jsonify({"message": f"User {data['username']} not updated"}), 200
    except:
        abort(500)