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
    

