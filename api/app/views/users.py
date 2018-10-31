""" file with all user routes """

import datetime

from flask_jwt_extended import ( 
    jwt_required, 
    create_access_token,
    get_jwt_identity
)
from flask import jsonify, abort, request
from api.app import app
from api.app.models.users import User


@app.route('/api/v1/auth/signup', methods=['POST'])
@jwt_required
def add_new_user():
    """ add new user method """

    logged_in_user = get_jwt_identity()

    if logged_in_user["role"] == "attendant":
        return jsonify({"message": "Unauthorized Access"})

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
@jwt_required
def view_all_users():
    """ get all registered users"""

    logged_in_user = get_jwt_identity()

    if logged_in_user["role"] == "attendant":
        return jsonify({"message": "Unauthorized Access"})

    user_class = User()
    users = user_class.get_all_registered_users()

    if len(users) == 0:
        return jsonify({"message": "No users registered yet"}), 404

    return jsonify({"users": users}), 200

@app.route('/api/v1/users/<int:user_id>/', methods=['GET'])
@jwt_required
def view_a_registered_user_details(user_id):
    """" get a specific registered user """

    logged_in_user = get_jwt_identity()

    if logged_in_user["role"] == "attendant":
        return jsonify({"message": "Unauthorized Access"})

    user_class = User()
    user = user_class.get_a_registered_user_by_id(user_id)

    if len(user) == 0:
        return jsonify({"message": "The User doesn't exist"}), 404

    return jsonify({"user": user}), 200

@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
@jwt_required
def edit_a_speific_user_details(user_id):
    """ modify or update a specific user's details """

    logged_in_user = get_jwt_identity()

    if logged_in_user["role"] == "attendant":
        return jsonify({"message": "Unauthorized Access"})

    data = request.json

    try:
        user_class = User()
        user = user_class.get_a_registered_user_by_id(user_id)

        if len(user) == 0:
            return jsonify({"message": "The User doesn't exist"}), 404
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
                return jsonify({"message": "The User doesn't exist"}), 404
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

    
@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
@jwt_required
def delete_a_registered_user(user_id):
    """ Remove or delete a specific user """

    logged_in_user = get_jwt_identity()

    if logged_in_user["role"] == "attendant":
        return jsonify({"message": "Unauthorized Access"})

    user_class = User()
    user = user_class.get_a_registered_user_by_id(user_id)

    if len(user) == 0:
        return jsonify({"message": "The User doesn't exist"}), 404
    else:
        deleted_user = user_class.remove_a_specific_user(user_id)    
        return jsonify({"message": f"{deleted_user} removed"}), 200

@app.route('/api/v1/auth/login', methods=['POST'])
def user_login():
    """ logging a user into the system """

    data = request.json

    if ("username" not in data or data["username"] == ""):
        return jsonify({"error": "Provide User username"})
    elif (isinstance(data["username"], (int, float))):
        return jsonify({"error": "Invalid User username"})

    if ("password" not in data or data["password"] == ""):
        return jsonify({"error": "Provide User password"})

    username = data["username"]
    password = data["password"]
    
    user_class = User()
    user = user_class.user_login(username, password)

    if user:
        if user[3] is True:
            logged_in = { 
                "role" : "admin",
                "id": user[0],
                "username" : user[1]
            }
        else:
            logged_in = { 
                "role" : "attendant",
                "id" : user[0],
                "username" : user[1]
            }

        token = create_access_token(identity = logged_in, expires_delta = datetime.timedelta(days=1))
        return jsonify({"message": f"User logged In as {logged_in['role']}", "login_token" : token}), 200
    else:
        return jsonify({"message": "Wrong login Credentials"}), 404

@app.route('/api/v1/auth/logout', methods=['DELETE'])
@jwt_required
def user_logout():
    """ logging a user out of the system """

    logged_in_user = get_jwt_identity()

    return jsonify({"message": f"{logged_in_user['username']} Logged out"}), 200