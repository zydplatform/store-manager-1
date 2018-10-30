""" User file for handling user operations """

from api.app.models.database import Database

class User(Database):
    """ User Class for handling users """

    def __init__(self):
        """ initialising User """
        super().__init__()

    def register_user(self, id_number, full_name, username, password):
        attendant = {
            "id_number" : id_number,
            "fullname" : full_name,
            "username" : username,
            "password" : password
        }

        get_registered_attendant_query = "SELECT * FROM users"

        self.cursor.execute(get_registered_attendant_query)

        attendants = self.cursor.fetchall()

        if attendant in attendants or [
                                    attendant for attendant in attendants
                                    if attendant[0] ==  id_number
                                    and attendant[3] == username
                                ]:
            return False

        else:
            register_attendant_query = """
                INSERT INTO users
                (id_number, full_name, username, password, registered_by)
                VALUES (%s, %s, %s, %s, %s);
            """
            self.cursor.execute(register_attendant_query, 
                (id_number, full_name, username, password, 0)
            )
            self.connection.commit()
            return True
    
    def get_all_registered_users(self):
        """ get all registered users from database """

        get_registered_attendant_query = "SELECT * FROM users"
        self.cursor.execute(get_registered_attendant_query)
        registered_users = self.cursor.fetchall()

        if registered_users == None:
            return {}
        
        users = []

        for registered_user in registered_users:
            user = {
                "user_id" : registered_user[0],
                "id_number" : registered_user[1],
                "full_name" : registered_user[2],
                "username" : registered_user[3],
                "password" : registered_user[4],
                "admin" : registered_user[5],
                "registered_by" :  registered_user[6],
                "registered_on" : registered_user[7]
            }
            users.append(user)

        return users

    def get_a_registered_user_by_id(self, user_id):
        """ get a specific user from the database """

        get_a_registered_attendant_query = "SELECT * FROM users WHERE user_id = %s"
        self.cursor.execute(get_a_registered_attendant_query, str(user_id))
        registered_user = self.cursor.fetchone()
            
        if registered_user == None:
            return {}
        
        user = {
            "user_id" : registered_user[0],
            "id_number" : registered_user[1],
            "full_name" : registered_user[2],
            "username" : registered_user[3],
            "password" : registered_user[4],
            "admin" : registered_user[5],
            "registered_by" :  registered_user[6],
            "registered_on" : registered_user[7]
        }

        return user

    def update_a_user_details(self, user_id, id_number, full_name, username, password, admin, registered_by):
        """ modify a specific user details """

        get_a_registered_attendant_query = "SELECT * FROM users WHERE user_id = %s"
        self.cursor.execute(get_a_registered_attendant_query, str(user_id))
        registered_user = self.cursor.fetchone()
        username = registered_user[3]

        if len(registered_user) == 0:
            return False
        else:
            update_user_query = """
                UPDATE users SET 
                id_number = %s,
                full_name = %s,
                username = %s,
                password = %s,
                admin = %s,
                registered_by = %s
                WHERE user_id = %s
            """

            self.cursor.execute(update_user_query, (id_number, full_name, username, password, admin, registered_by, str(user_id)))
            self.connection.commit()

            return username

    def remove_a_specific_user(self, user_id):
        """ delete or remove a specific user """

        get_a_registered_attendant_query = "SELECT * FROM users WHERE user_id = %s"
        self.cursor.execute(get_a_registered_attendant_query, str(user_id))
        registered_user = self.cursor.fetchone()
        username = registered_user[3]

        delete_a_user_query = "DELETE FROM users WHERE user_id = %s"
        self.cursor.execute(delete_a_user_query, str(user_id))
        self.connection.commit()

        return username

    def user_login(self, username, password):
        """ checking a user login credentials """

        check_user_credentials_query = "SELECT username, password, admin FROM users WHERE username = %s AND password = %s;"

        self.cursor.execute(check_user_credentials_query, (username, password))    
        login_user = self.cursor.fetchone()

        if login_user == None:
            return False
        else:
            return login_user