""" User file for handling user operations """

from api.app.models.database import Database

class User(Database):
    """ User Class for handling users """

    def __init__(self):
        """ initialising User """
        super().__init__()


    def register_user(self, full_name, email, password, registered_by):
        user = {
            "fullname" : full_name,
            "email" : email,
            "password" : password
        }

        get_all_registered_users_query = "SELECT * FROM users"

        self.cursor.execute(get_all_registered_users_query)

        registered_users = self.cursor.fetchall()

        if user in registered_users or [
                                    registered_user for registered_user in registered_users
                                    if registered_user[2] == email
                                ]:
            return False

        else:
            register_user_query = """
                INSERT INTO users
                (full_name, email, password, registered_by)
                VALUES (%s, %s, %s, %s);
            """
            self.cursor.execute(register_user_query, 
                (full_name, email, password, registered_by)
            )
            self.connection.commit()
            
            registered_user_query = "SELECT * FROM users WHERE user_id = currval(pg_get_serial_sequence('users','user_id'));"
            self.cursor.execute(registered_user_query)
            registered_user = self.cursor.fetchone()            

            return registered_user
    
    def get_all_registered_users(self):
        """ get all registered users from database """

        get_registered_users_query = "SELECT * FROM users"
        self.cursor.execute(get_registered_users_query)
        registered_users = self.cursor.fetchall()

        if registered_users == None:
            return {}
        
        users = []

        for registered_user in registered_users:
            user = {
                "user_id" : registered_user[0],
                "full_name" : registered_user[1],
                "email" : registered_user[2],
                "password" : registered_user[3],
                "admin" : registered_user[4],
                "registered_by" :  registered_user[5],
                "registered_on" : registered_user[6]
            }
            users.append(user)

        return users

    def get_a_registered_user_by_id(self, user_id):
        """ get a specific user from the database """

        get_a_registered_user_query = "SELECT * FROM users WHERE user_id = %s"
        self.cursor.execute(get_a_registered_user_query, str(user_id))
        registered_user = self.cursor.fetchone()
            
        if registered_user == None:
            return {}
        
        user = {
            "user_id" : registered_user[0],
            "full_name" : registered_user[1],
            "email" : registered_user[2],
            "password" : registered_user[3],
            "admin" : registered_user[4],
            "registered_by" :  registered_user[5],
            "registered_on" : registered_user[6]
        }

        return user

    def update_a_user_details(self, user_id, full_name, email, password, admin, updated_by):
        """ modify a specific user details """

        get_a_registered_user_query = "SELECT * FROM users WHERE user_id = %s"
        self.cursor.execute(get_a_registered_user_query, str(user_id))
        registered_user = self.cursor.fetchone()
        full_name = registered_user[1]

        if len(registered_user) == 0:
            return False
        else:
            update_user_query = """
                UPDATE users SET
                full_name = %s,
                email = %s,
                password = %s,
                admin = %s,
                registered_by = %s
                WHERE user_id = %s
            """

            self.cursor.execute(update_user_query, (full_name, email, password, admin, updated_by, str(user_id)))
            self.connection.commit()

            return full_name

    def remove_a_specific_user(self, user_id):
        """ delete or remove a specific user """

        get_a_registered_user_query = "SELECT * FROM users WHERE user_id = %s"
        self.cursor.execute(get_a_registered_user_query, str(user_id))
        registered_user = self.cursor.fetchone()
        full_name = registered_user[1]

        delete_a_user_query = "DELETE FROM users WHERE user_id = %s"
        self.cursor.execute(delete_a_user_query, str(user_id))
        self.connection.commit()

        return full_name

    def user_login(self, email):
        """ checking a user login credentials """

        check_user_credentials_query = "SELECT * FROM users WHERE email = %s"

        self.cursor.execute(check_user_credentials_query, (email,))    
        login_user = self.cursor.fetchone()

        if login_user == None:
            return False
        else:
            return login_user