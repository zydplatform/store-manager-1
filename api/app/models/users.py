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